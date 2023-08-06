import itertools
import json
import logging
import os
import pathlib
import subprocess
import sys
import tarfile
import tempfile
import time
from typing import Callable, Dict, List, Optional, Sequence, Tuple, Union

import attr
import docker
import jsondiff
import jsonschema
from docker.errors import APIError
from semantic_version import Version

from r2c.cli.util import check_docker_is_running  # type: ignore
from r2c.cli.util import find_and_open_analyzer_manifest  # type: ignore
from r2c.lib.analysis import AnalysisRunner, OutputStorage
from r2c.lib.analyzer import AnalyzerName, SpecifiedAnalyzer, VersionedAnalyzer
from r2c.lib.filestore import (
    LocalFilesystemOutputStore,
    LocalJsonOutputStore,
    LocalLogStore,
    LocalStatsStore,
)
from r2c.lib.input import AnalyzerInput, LocalCode
from r2c.lib.jobdef import CacheKey
from r2c.lib.manifest import (
    AnalyzerDependency,
    AnalyzerManifest,
    AnalyzerOutputType,
    LinkedAnalyzerNameMismatch,
)
from r2c.lib.registry import RegistryData
from r2c.lib.util import get_tmp_dir, get_unique_semver, sort_two_levels, url_to_repo_id

TEST_VECTOR_FOLDER = "examples"  # folder with tests
TMP_DIR = get_tmp_dir()
INTEGRATION_TEST_DIR_PREFIX = os.path.join(TMP_DIR, "analysis-integration-")
LOCAL_RUN_TMP_FOLDER = os.path.join(
    TMP_DIR, "local-analysis", ""
)  # empty string to ensure trailing /
CONTAINER_MEMORY_LIMIT = "2G"
UNITTEST_CMD = "/analyzer/unittest.sh"
UNITTEST_LOCATION = "src/unittest.sh"
EXPERIMENTAL_BUILD = "ExperimentalBuild"
logger = logging.getLogger(__name__)
ANALYSIS_CACHE_DIR = os.path.join(TMP_DIR, "analysis-cache")


def clone_repo(url, hash, target_path):
    logger.info(f"cloning for integration tests: {url} into {target_path}")
    subprocess.check_call(["git", "clone", "--quiet", url, target_path])
    subprocess.check_call(["git", "checkout", hash, "--quiet"], cwd=target_path)


@attr.s(auto_attribs=True)
class InvalidAnalyzerIntegrationTestDefinition(Exception):
    """Thrown when the analyzer's integration test doesn't conform to its schema."""

    inner: Union[jsonschema.ValidationError, json.JSONDecodeError]


def validator_for_test(
    test_filename: str, test_case_js: dict, manifest: AnalyzerManifest
) -> Callable[[str], bool]:
    def validator(analyzer_output_path: str) -> bool:
        output = json.load(open(analyzer_output_path))

        # make sure the integration tests are match the schema for integration tests for this version of the output spec
        try:
            manifest.output.integration_test_validator(output).validate(test_case_js)
        except jsonschema.ValidationError as err:
            logger.error(
                f"invalid integration test (does not follow schema): {test_filename}"
            )
            raise InvalidAnalyzerIntegrationTestDefinition(err) from err

        # we only want to sort two levels--the dicts and their keys. We don't
        # want to recurse and sort into the "extra" key that may be present
        diff = jsondiff.diff(
            sort_two_levels(test_case_js["expected"]),
            sort_two_levels(output["results"]),
        )
        if len(diff) > 0:
            logger.error(
                f"\n❌ test vector failed, actual output did not match expected for: {test_filename}, check {analyzer_output_path} and see below for diff:\n\n{diff}\n\n"
            )
            return False
        else:
            logger.error(f"\n✅ test vector passed: {test_filename}")
            return True

    return validator


def integration_test(
    manifest: AnalyzerManifest,
    analyzer_directory: str,
    verbose: bool,
    env_args_dict: Dict[str, str],
    registry_data: RegistryData,
    use_cache: bool = False,
) -> bool:
    test_vectors_path = os.path.join(analyzer_directory, TEST_VECTOR_FOLDER)
    test_vectors: Sequence[str] = []
    if os.path.isdir(test_vectors_path):
        test_vectors = [f for f in os.listdir(test_vectors_path) if f.endswith(".json")]
    if len(test_vectors) > 0:
        logger.info(
            f"Found {len(test_vectors)} integration test vectors in {test_vectors_path}"
        )
    else:
        logger.warning(
            f"⚠️ No integration test vectors in examples directory: {test_vectors_path}"
        )

    results: Dict[str, bool] = {}
    test_times = {}
    for test_filename in test_vectors:
        logger.info(f"Starting test: {test_filename}")
        test_path = os.path.join(test_vectors_path, test_filename)
        with open(test_path) as test_content:
            try:
                js = json.load(test_content)
            except json.decoder.JSONDecodeError as ex:
                logger.error(f"invalid json in file: {test_path}: {str(ex)}")
                sys.exit(1)
            test_target = js["target"]
            test_target_hash = js["target_hash"]
            with tempfile.TemporaryDirectory(
                prefix=INTEGRATION_TEST_DIR_PREFIX
            ) as tempdir:
                clone_repo(test_target, test_target_hash, tempdir)
                validator = validator_for_test(
                    test_filename=test_filename, test_case_js=js, manifest=manifest
                )
                start_time = time.time()
                test_result = run_analyzer_on_local_code(
                    registry_data,
                    manifest=manifest,
                    analyzer_dir=analyzer_directory,
                    analyzer_input=LocalCode(tempdir),
                    show_output_on_stdout=verbose,
                    pass_analyzer_output=True,
                    output_path=None,
                    interactive=None,
                    env_args_dict=env_args_dict,
                    reset_cache=not use_cache,
                    validator=validator,
                )
                results[test_path] = bool(test_result)
                test_times[test_path] = time.time() - start_time

    results_str = ""
    for test_path, result in results.items():
        status = "✅ passed" if result else "❌ failed"
        time_str = time.strftime("%H:%M:%S", time.gmtime(test_times[test_path]))
        results_str += f"\n\t{status}: {test_path} (time: {time_str})"
    # print to stdout
    print(results_str)
    num_passing = len([r for r in results.values() if r is True])
    print("##############################################")
    print(f"summary: {num_passing}/{len(results)} passed")
    if len(results) != num_passing:
        logger.error("integration test suite failed")
        return False
    else:
        return True


def run_docker_unittest(
    analyzer_directory, analyzer_name, docker_image, verbose, env_args_dict
):
    env_args = list(
        itertools.chain.from_iterable(
            [["-e", f"{k}={v}"] for (k, v) in env_args_dict.items()]
        )
    )
    path = os.path.join(analyzer_directory, UNITTEST_LOCATION)
    if verbose:
        logger.info(f"Running unittest by executing {path}")
    if not os.path.exists(path):
        logger.warn(f"no unit tests for analyzer: {analyzer_name}")
        return 0
    docker_cmd = (
        ["docker", "run", "--rm"] + env_args + [f"{docker_image}", f"{UNITTEST_CMD}"]
    )
    if not verbose:
        docker_cmd.append(">/dev/null")
    if verbose:
        logger.error(f"running with {' '.join(docker_cmd)}")
    status = subprocess.call(docker_cmd)
    return status


def pull_docker(va: VersionedAnalyzer) -> int:
    try:
        client = docker.from_env()
        logger.info(f"Pulling image {va.image_id} from remote registry")
        client.images.pull(va.image_id)
    except APIError:
        logger.error(
            f"Docker pull failed on analyzer {va.name}. Check you are logged in via `r2c login`"
        )
        return -1
    except Exception as e:
        logger.exception(f"Something happened while pulling {va.name}", e)
        return -1
    return 0


def build_docker(
    analyzer_name: AnalyzerName,
    version: Version,
    docker_context: str,
    dockerfile_path: Optional[str] = None,
    env_args_dict: Dict = {},
    no_cache: Optional[bool] = False,
    squash: Optional[bool] = False,
) -> int:
    info = check_docker_is_running()
    docker_image = VersionedAnalyzer(analyzer_name, version).image_id
    if not dockerfile_path:
        dockerfile_path = f"{docker_context}/Dockerfile"
    extra_build_args = [f"--build-arg {k}={v}" for (k, v) in env_args_dict.items()]
    build_cmd = (
        f"docker build -t {docker_image} -f {dockerfile_path} {docker_context} "
        + " ".join(extra_build_args)
    )
    if no_cache:
        build_cmd += " --no-cache"
    # --squash is supported in experimental
    if squash and info:
        if info.get(EXPERIMENTAL_BUILD):
            build_cmd += " --squash"
        else:
            raise Exception(
                "`--squash` is only supported on a Docker daemon with experimental features enabled. Enable experimental features by Preferences -> Daemon -> Experimental features. "
            )
    build_cmd += " 1>&2"

    logger.debug(f"building with build command: {build_cmd}")
    status = subprocess.call(build_cmd, shell=True)
    return status


def setup_locally_linked_analyzer(
    manifest: AnalyzerManifest, registry_data: RegistryData, analyzer_directory: str
) -> RegistryData:
    """
        Build and tags analyzer in ANALYZER_DIRECTORY with a unique version
        and returns a modified registry so that local runs will resolve to said built analyzer.
    """

    new_registry = registry_data.deepcopy()
    new_dependencies: List[AnalyzerDependency] = []
    for dep in manifest.dependencies:
        if not dep.path:
            new_dependencies.append(dep)
            continue
        try:
            local_manifest, local_dir = find_and_open_analyzer_manifest(
                os.path.normpath(os.path.join(analyzer_directory, dep.path))
            )
        except Exception as e:
            logger.debug(
                f"Exception while resolving local linked dependendies: {str(e)}"
            )
            raise e
        # validate name
        if local_manifest.analyzer_name != dep.name:
            raise LinkedAnalyzerNameMismatch(
                f"Linked analyzer name must match {local_manifest.analyzer_name} != {dep.name}"
            )

        # build docker with unique version
        local_version = get_unique_semver(local_manifest.version)
        build_docker(
            local_manifest.analyzer_name,
            local_version,
            os.path.relpath(local_dir, os.getcwd()),
        )

        # add linked dep to registry
        local_manifest.version = local_version
        new_registry = new_registry.add_pending_manifest(local_manifest, force=True)

        new_dependencies.append(
            AnalyzerDependency(
                AnalyzerName(local_manifest.analyzer_name),
                wildcard_version=str(local_version),
                parameters=dep.parameters,
            )
        )

    # add analyzer to registry
    manifest.dependencies = new_dependencies
    manifest.original_json["dependencies"] = {
        dep.name: {"version": dep.wildcard_version, "path": dep.path}
        for dep in new_dependencies
    }
    new_registry = new_registry.add_pending_manifest(manifest, force=True)
    return new_registry


def run_analyzer_on_local_code(
    registry_data: RegistryData,
    manifest: AnalyzerManifest,
    analyzer_dir: str,
    analyzer_input: AnalyzerInput,
    output_path: Optional[str],
    show_output_on_stdout: bool,
    pass_analyzer_output: bool,
    env_args_dict: dict,
    interactive: Optional[Union[int, str]] = None,
    reset_cache: bool = False,
    run_as_host_uid: bool = False,
    validator: Callable[[str], bool] = None,
    parameters: Optional[Dict[str, str]] = None,
) -> Optional[bool]:
    """Run an analyzer on a local folder. Returns the result of any validator, if
    present, or None if there was no validation performed.

    Args:
        input: if this is a LocalCode, all fetcher analyzers will have their output overridden with the contents of its directory. Else it's passed to the fetcher analyzers and run as normal.
        output_path: if supplied, the analyzer output file (ex output.json, fs.tar.gz), will be written to this local path
        show_output_on_stdout: show the analyzer output file on stdout
        pass_analyzer_output: if false, analyzer stdout and stderr will be supressed
        validator: a callable function that takes as its argument the output.json of an analyzer and returns whether it is valid for the analyzer's schema
        interactive: don't start the container - just shell into the container (specified by index or name) before anlayzer executes and exit
    """
    json_output_store = LocalJsonOutputStore()
    filesystem_output_store = LocalFilesystemOutputStore()
    log_store = LocalLogStore()
    stats_store = LocalStatsStore()

    cache_dir = pathlib.Path(ANALYSIS_CACHE_DIR)
    cache_dir.mkdir(exist_ok=True)
    output_storage = OutputStorage(
        json_output_store, filesystem_output_store, cache_dir=cache_dir
    )

    if reset_cache:
        json_output_store.delete_all()
        filesystem_output_store.delete_all()
        log_store.delete_all()
        output_storage.reset_cache()

    versioned_analyzer = VersionedAnalyzer(manifest.analyzer_name, manifest.version)

    if not manifest.is_locally_linked:
        # try adding the manifest of the current analyzer if it isn't already there
        if versioned_analyzer not in registry_data.versioned_analyzers:
            logger.info(
                "Analyzer manifest not present in registry. Adding it to the local copy of registry."
            )
            registry_data = registry_data.add_pending_manifest(manifest)
        else:
            logger.info("Analyzer manifest already present in registry")
    else:
        registry_data = setup_locally_linked_analyzer(
            manifest, registry_data, analyzer_dir
        )

    # Add any parameters required to specified_analyzer
    specified_analyzer = SpecifiedAnalyzer(
        versioned_analyzer.name, versioned_analyzer.version, parameters or {}
    )

    runner = AnalysisRunner(
        registry_data,
        output_storage,
        log_store,
        stats_store,
        timeout=0,
        pass_analyzer_output=pass_analyzer_output and show_output_on_stdout,
        memory_limit=CONTAINER_MEMORY_LIMIT,
        run_as_host_uid=run_as_host_uid,
        env_args_dict=env_args_dict,
    )

    # Delete any existing output for this analyzer. We do this even if
    # reset_cache is false because in general, when running locally you almost
    # never want to use cached results (since you're typically tweaking an
    # analyzer).
    cache_key = CacheKey(specified_analyzer, analyzer_input)
    json_output_store.delete(cache_key)
    filesystem_output_store.delete(cache_key)
    log_store.delete(cache_key)
    stats_store.delete(cache_key)

    runner.full_analyze_request(
        analyzer_input=analyzer_input,
        specified_analyzer=specified_analyzer,
        force=False,
        interactive=interactive,
    )

    # Can't use NamedTemporaryFile here because we are copying to the
    # file by name and not by the already opened file handle
    # Should wrap this in a context manager (https://github.com/returntocorp/echelon-backend/issues/2735)
    if not output_path:
        _, output_path_used = tempfile.mkstemp(dir=get_tmp_dir())
    else:
        output_path_used = output_path

    # Get Final Output
    if manifest.output_type == AnalyzerOutputType.json:
        json_output_store.get(cache_key, output_path_used)
    elif manifest.output_type == AnalyzerOutputType.filesystem:
        filesystem_output_store.get(cache_key, output_path_used)

    if show_output_on_stdout:
        logger.info(f"Analyzer output")
        logger.info("=" * 60)
        if tarfile.is_tarfile(output_path_used):
            with tarfile.open(output_path_used, "r") as tar:
                tar.list(verbose=False)
        else:
            with open(output_path_used, "r") as f:
                print(f.read())  # explicitly send this to stdout

    if validator:
        return validator(output_path_used)

    if not output_path:
        os.remove(output_path_used)
    else:
        logger.info(f"Wrote analyzer output to: {output_path_used}")

    return None


def get_local_git_origin_and_commit(dir: str) -> Tuple[str, str]:
    try:
        repo = (
            subprocess.check_output(
                ["git", "config", "--get", "remote.origin.url"], cwd=dir
            )
            .strip()
            .decode("utf-8")
        )
        commit = (
            subprocess.check_output(
                ["git", "show", '--format="%H"', "--no-patch"], cwd=dir
            )
            .strip()
            .decode("utf-8")
        )
        return repo, commit.replace('"', "")
    except subprocess.CalledProcessError:
        logger.error(f"failed to determine source git repo or commit for {dir}")
        # use same util function, but treat local relative dir path as repo
        hash_of_dir = url_to_repo_id(dir)
        logger.debug(f"Using {hash_of_dir}, {hash_of_dir} as repo, commit")
        return hash_of_dir, hash_of_dir
