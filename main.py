from fastapi import FastAPI, Request
import uvicorn
from pydantic import BaseModel, Field
from typing import List, Any, Dict

from worker import create_multi_tasks, get_tasks_completion, get_results


from cities import cities


class TaskRequest(BaseModel):
    id: str


class TaskCompletion(BaseModel):
    completed_percentage: float = Field(ge=0, le=100)


class Result(BaseModel):
    results: List[Dict]


app = FastAPI()


@app.post("/tasks", status_code=201)
async def run_task(task_request: TaskRequest):
    create_multi_tasks(task_request.id, cities)
    return {"id": task_request.id}


@app.get("/completion", status_code=200)
async def get_completed(request: Request):
    params = dict(request.query_params)

    return TaskCompletion(completed_percentage=get_tasks_completion(params["id"]))


@app.get("/results", status_code=200)
async def get_completed(request: Request):
    params = dict(request.query_params)

    return Result(results=get_results(params["id"]))


if __name__ == "__main__":
    uvicorn.run(app, port=8080, host="0.0.0.0")
