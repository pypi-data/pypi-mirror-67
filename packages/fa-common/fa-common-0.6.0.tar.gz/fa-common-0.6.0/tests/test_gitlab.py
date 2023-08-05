import os
import pytest

import oyaml as yaml
from fa_common import create_app, start_app, utils, force_sync
from fa_common.gitlab import (
    get_gitlab_client,
    run_job,
    ScidraModule,
    FileDownloadRef,
    get_job_run,
    get_job_log,
    create_workflow_project,
)
from .conftest import get_env_file, TEST_GITLAB_PROJECT, TEST_GITLAB_BRANCH

dirname = os.path.dirname(__file__)
test_data_path = os.path.join(dirname, "data")

app = create_app(env_path=get_env_file())
force_sync(start_app)(app)
utils.current_app = app


@pytest.mark.asyncio
async def test_gitlab_create(ensure_no_test_gitlab):
    client = get_gitlab_client()
    workflow_project = await create_workflow_project(
        TEST_GITLAB_PROJECT, TEST_GITLAB_BRANCH
    )

    assert workflow_project.gitlab_project_id > 0
    assert workflow_project.name == TEST_GITLAB_BRANCH

    with open(os.path.join(dirname, test_data_path, "job.yaml"), "r") as file:
        # The FullLoader parameter handles the conversion from YAML
        # scalar values to Python the dictionary format
        job_file = yaml.safe_load(file)

    commit_id = await client.update_ci(
        workflow_project.gitlab_project_id, workflow_project.name, job_file, "Unit Test"
    )
    assert commit_id


@pytest.mark.asyncio
async def test_job_create(ensure_test_gitlab):
    project_id = ensure_test_gitlab
    assert project_id > 0

    module = ScidraModule(
        name="noise-detection",
        docker_image="docker-registry.it.csiro.au/scidra-modules/noise-detection:latest",
    )
    job_data = {
        "window_channels": 4,
        "window_size": 20,
        "channel_step": 2,
        "window_step": 10,
        "variation_threshold": 0.01,
        "crossover_threshold": 0.003,
    }
    files = [
        FileDownloadRef(
            name="data_file",
            url="https://firebasestorage.googleapis.com/v0/b/gp-toolkit-staging.appspot.com/o/"
            + "unit_test_data%2Fnd_test_data.csv?alt=media&token=96a65aa1-9e34-4a37-9bc7-7eac4f14847e",
            extension="csv",
        )
    ]

    job_run = await run_job(
        project_id, "test_project", "Sync Unit Test", module, job_data, files, sync=True
    )

    assert job_run.status == "success"
    assert job_run.output is not None

    job_run2 = await get_job_run(project_id, job_run.id, True)

    assert job_run2.id == job_run.id


@pytest.mark.asyncio
async def test_job_create_async(ensure_test_gitlab):
    project_id = ensure_test_gitlab
    assert project_id > 0

    module = ScidraModule(
        name="noise-detection",
        docker_image="docker-registry.it.csiro.au/scidra-modules/noise-detection:latest",
    )
    job_data = {
        "window_channels": 4,
        "window_size": 20,
        "channel_step": 2,
        "window_step": 10,
        "variation_threshold": 0.01,
        "crossover_threshold": 0.003,
    }
    files = [
        FileDownloadRef(
            name="data_file",
            url="https://firebasestorage.googleapis.com/v0/b/gp-toolkit-staging.appspot.com/o/"
            + "unit_test_data%2Fnd_test_data.csv?alt=media&token=96a65aa1-9e34-4a37-9bc7-7eac4f14847e",
            extension="csv",
        )
    ]

    job_run = await run_job(
        project_id, "test_project", "Async Unit Test", module, job_data, files
    )

    job_run2 = await get_job_run(project_id, job_run.id)

    assert job_run2.id == job_run.id
    job_logs = await get_job_log(project_id, job_run.id)
