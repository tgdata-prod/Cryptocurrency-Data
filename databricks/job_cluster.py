from databricks.sdk import WorkspaceClient
from databricks.sdk.service.jobs import Task, NotebookTask, Source
from dotenv import load_dotenv
import os 

load_dotenv()

CLUSTER_ID=os.getenv("CLUSTER_ID")
CLUSTER_NAME=os.getenv("CLUSTER_NAME")

w = WorkspaceClient()

job_name            = 'my-job'
description         = 'run a job'
existing_cluster_id = CLUSTER_ID
notebook_path       = '/databricks/TomsNotebook.ipynb'
task_key            = 'Toms-Key'

print("Attempting to create the job. Please wait...\n")

j = w.jobs.create(
  name = job_name,
  tasks = [
    Task(
      description = description,
      existing_cluster_id = CLUSTER_ID,
      notebook_task = NotebookTask(
        base_parameters = dict(""),
        notebook_path = notebook_path,
        source = Source("WORKSPACE")
      ),
      task_key = task_key
    )
  ]
)

print(f"View the job at {w.config.host}/#job/{j.job_id}\n")
