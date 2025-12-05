from databricks.sdk import WorkspaceClient
from databricks.sdk.service.jobs import NotebookTask, Source, Task

w = WorkspaceClient()

j = w.jobs.create(
  name = "My Serverless Job",
  tasks = [
    Task(
      notebook_task = NotebookTask(
      notebook_path = "/databricks/TomsNotebook.ipynb",
      source = Source("WORKSPACE")
      ),
      task_key = "MyTask",
   )
  ]
)
