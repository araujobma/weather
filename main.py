from fastapi import FastAPI, Request, Response, status
import uvicorn
from pydantic import BaseModel, Field
from model import WeatherTask
from typing import List, Dict

from worker import create_multi_tasks, get_tasks_completion, get_task_results


from cities import cities


class TaskRequest(BaseModel):
    id: str | None = None


class TaskCompletion(BaseModel):
    completed_percentage: float = Field(ge=0, le=100, default=None)


class Result(BaseModel):
    results: List[Dict] | None = None


app = FastAPI()


@app.post("/tasks", status_code=201)
async def run_task(task_request: TaskRequest, response: Response) -> TaskRequest:
    existing_task = WeatherTask.get_by_id(task_request.id)
    if existing_task:
        response.status_code = status.HTTP_200_OK
        return TaskRequest(id=task_request.id)

    task_group_id = create_multi_tasks(task_request.id, cities)
    task = WeatherTask(id=task_request.id, task_group_id=task_group_id)
    task.save()

    return TaskRequest(id=task_request.id)


@app.get("/completion/{id}", status_code=200)
async def get_completion(id, response: Response) -> TaskCompletion:

    task = WeatherTask.get_by_id(id)
    if not task:
        response.status_code = status.HTTP_404_NOT_FOUND
        return TaskCompletion()

    task_group_id = task.task_group_id

    return TaskCompletion(completed_percentage=get_tasks_completion(task_group_id))


@app.get("/results/{id}", status_code=200)
async def get_results(id, response: Response) -> Result:

    task = WeatherTask.get_by_id(id)
    if not task:
        response.status_code = status.HTTP_404_NOT_FOUND
        return Result()

    task_group_id = task.task_group_id

    return Result(results=get_task_results(task_group_id))


if __name__ == "__main__":
    uvicorn.run(app, port=8080, host="0.0.0.0")
