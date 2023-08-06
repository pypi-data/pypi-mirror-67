import os
import subprocess
from typing import Optional

import click

from r2c.cli.commands.cli import cli
from r2c.cli.logger import (
    abort_on_build_failure,
    get_logger,
    print_error_exit,
    print_exception_exit,
    print_msg,
    print_success,
    print_success_step,
)
from r2c.cli.network import (
    auth_post,
    auth_put,
    docker_login,
    get_base_url,
    get_docker_creds,
    handle_request_with_error_message,
)
from r2c.cli.run import build_docker
from r2c.cli.util import (
    find_and_open_analyzer_manifest,
    find_and_open_analyzer_readme,
    get_default_org,
    get_org_from_analyzer_name,
    parse_remaining,
)
from r2c.lib.analyzer import VersionedAnalyzer
from r2c.lib.constants import PLATFORM_ANALYZER_PREFIX
from r2c.lib.manifest import AnalyzerManifest


def _docker_push(image_id: str) -> bool:
    """Pushes docker image to ECR using docker credentials"""
    docker_push_cmd = f"docker push {image_id}"
    docker_push_cmd += " 1>&2"
    get_logger().debug(f"Running push with command: {docker_push_cmd}")
    return_code = subprocess.call(docker_push_cmd, shell=True)
    return return_code == 0


def _upload_analyzer_manifest(
    manifest: AnalyzerManifest, force: bool, readme: Optional[str] = None
) -> str:
    get_logger().info(f"Uploading manifest")
    analyzer_json = manifest.to_json()
    if "readme" not in analyzer_json and readme:
        analyzer_json["readme"] = readme
    # this unwrapping thing is ugly, but we have to do it for backwards compatibility
    # since we can't add a manifest field
    r = auth_post(
        f"{get_base_url()}/api/v1/analyzers/", json={**analyzer_json, "force": force}
    )
    data = handle_request_with_error_message(r)
    link = data.get("links", {}).get("artifact_url")
    return link


@cli.command()
@click.option(
    "-A",
    "--analyzer-directory",
    default=os.getcwd(),
    help="The directory where the analyzer is located, defaulting to the current directory.",
)
@click.option(
    "--force",
    is_flag=True,
    default=True,
    help="Overwrite analyzer of the same name and version if it exists in the registry as pending (its corresponding image hasn't been uploaded). "
    "This is usually useful for cases when an image upload was aborted or failed.",
)
@click.option(
    "--squash",
    is_flag=True,
    default=False,
    help="Squash newly built docker layers into a single new layer before pushing to `r2c`",
)
@click.argument("env_args_string", nargs=-1, type=click.Path())
@click.pass_context
def push(ctx, analyzer_directory, force, squash, env_args_string):
    """
    Push the analyzer in the current directory to the R2C platform.

    You must log in to push analyzers.

    This command will validate your analyzer and privately publish your analyzer
    to your org with the name specified in analyzer.json.

    Your analyzer name must follow {org}/{name}.
    """
    env_args_dict = parse_remaining(env_args_string)

    manifest, analyzer_directory = find_and_open_analyzer_manifest(
        analyzer_directory, ctx
    )
    readme = find_and_open_analyzer_readme(analyzer_directory, ctx)
    analyzer_org = get_org_from_analyzer_name(manifest.analyzer_name)

    overwriting_message = (
        " and forcing overwrite if the analyzer version exists and is pending upload."
    )
    # TODO(ulzii): let's decide which source of truth we're using for analyzer_name above and/or check consistency.
    # can't have both dir name and what's in analyzer.json
    print_msg(
        f"📌 Pushing analyzer in {analyzer_directory}{overwriting_message if force else ''}..."
    )

    default_org = get_default_org()
    if default_org is None:
        print_error_exit(
            f"You are not logged in. Please run `r2c login` to be able to push your analyzer"
        )

    if default_org != analyzer_org:
        if analyzer_org != PLATFORM_ANALYZER_PREFIX:
            print_error_exit(
                f"You're logged in to the common r2c platform. The org specified as the prefix of your analyzer name in `analyzer.json` must be `{PLATFORM_ANALYZER_PREFIX}`. "
                + f"Replace `{analyzer_org}` with `{PLATFORM_ANALYZER_PREFIX}` and try again."
                + "Please ask for help from r2c support"
            )
    try:
        # upload analyzer.json
        artifact_link = _upload_analyzer_manifest(manifest, force, readme)
    except Exception as e:
        print_exception_exit("There was an error uploading your analyzer", e)
    if artifact_link is None:
        print_error_exit(
            "There was an error uploading your analyzer. Please ask for help from R2C support"
        )
    get_logger().info(f"using artifact link: {artifact_link}")
    # get docker login creds
    creds = get_docker_creds(artifact_link)
    if creds is None:
        print_error_exit(
            "There was an error getting Docker credentials. Please ask for help from R2C support"
        )
    else:
        print_success_step("Successfully fetched credentials.")

    # docker login
    successful_login = docker_login(creds)
    if not successful_login:
        print_error_exit(
            "There was an error logging into Docker. Please ask for help from R2C support"
        )
    else:
        print_success_step("Successfully logged in to docker.")

    print_msg("🔨 Building docker container")
    # docker build and tag
    abort_on_build_failure(
        build_docker(
            manifest.analyzer_name,
            manifest.version,
            os.path.relpath(analyzer_directory, os.getcwd()),
            env_args_dict=env_args_dict,
            squash=squash,
        )
    )
    # docker push
    image_id = VersionedAnalyzer(manifest.analyzer_name, manifest.version).image_id
    print_msg(f"Pushing docker container to `{analyzer_org}`")
    successful_push = _docker_push(image_id)
    if not successful_push:
        print_error_exit(
            "There was an error pushing the Docker image. Please ask for help from R2C support"
        )
    else:
        print_success_step("Successfully pushed to R2C.")
    # mark uploaded with API
    # TODO figure out how to determine org from analyzer.json
    try:
        uploaded_url = f"{get_base_url()}/api/v1/analyzers/{manifest.analyzer_name}/{manifest.version}/uploaded"
        r = auth_put(uploaded_url)
        data = handle_request_with_error_message(r)
        if data.get("status") == "uploaded":
            web_url = data["links"]["web_url"]
            # display status to user and give link to view in web UI
            print_success(
                f"Upload finished successfully for analyzer! Visit: {web_url}"
            )
        else:
            print_error_exit("Error confirming analyzer was successfully uploaded.")
    except Exception as e:
        print_exception_exit("Error confirming analyzer was successfully uploaded", e)
