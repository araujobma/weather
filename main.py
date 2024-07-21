from fastapi import FastAPI
import uvicorn
import os
from worker import create_task


app = FastAPI()


@app.post("/tasks", status_code=201)
async def run_task():
    print("run task")
    task = create_task.delay(1)
    return {"task_id": task.id}


if __name__ == "__main__":
    uvicorn.run(app, port=8080, host="0.0.0.0")
