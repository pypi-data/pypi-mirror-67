import os
import json
from datetime import datetime
from typing import List
from .models import ScidraModule, FileDownloadRef, JobRun, WorkflowProject
from .utils import get_gitlab_client
from fa_common import logger as LOG
import oyaml as yaml

dirname = os.path.dirname(__file__)


async def create_workflow_project(user_id: str, project_name: str) -> WorkflowProject:
    client = get_gitlab_client()
    try:
        project = await client._get_project_by_name(user_id)
    except ValueError:
        project = await client.create_project(user_id)

    branch = await client.create_branch(project.id, project_name)

    return WorkflowProject(
        name=branch.name,
        user_id=user_id,
        gitlab_project_id=project.id,
        created=str(datetime.now()),
    )


async def run_job(
    user_id: str,
    workflow_project_id: str,
    description: str,
    module: ScidraModule,
    job_data: dict,
    files: List[FileDownloadRef] = [],
    sync: bool = False,
) -> JobRun:

    file_refs = []
    for _file in files:
        file_refs.append(_file.dict())

    with open(os.path.join(dirname, "job.yml")) as yaml_file:
        job_yaml = yaml.safe_load(yaml_file)

    job_yaml["run-job"]["image"] = module.docker_image
    job_yaml["run-job"]["variables"]["JOB_PARAMETERS"] = json.dumps(job_data)
    job_yaml["run-job"]["variables"]["FILE_REFS"] = json.dumps(file_refs)

    LOG.info(job_yaml)

    client = get_gitlab_client()

    await client.update_ci(user_id, workflow_project_id, job_yaml, description)
    job_run = await client.run_pipeline(user_id, workflow_project_id, wait=sync)
    return job_run.jobs[0]


async def get_job_run(user_id: str, job_id: int, include_log: bool = False) -> JobRun:
    client = get_gitlab_client()
    return await client.get_job(user_id, job_id, include_log)


async def get_job_log(user_id: str, job_id: int):
    client = get_gitlab_client()
    logs = await client.get_job_log(user_id, job_id)
    return logs
