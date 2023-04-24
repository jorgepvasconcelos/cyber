import uvicorn
from fastapi import FastAPI
from pydantic import BaseModel

from task_app.send_task import send_task

app = FastAPI()


class TaskDeliver(BaseModel):
    task_name: str


@app.post(path="/task_deliver")
async def task_deliverer(task:TaskDeliver):
    result_task = send_task(task_name=task.task_name)
    return result_task.task_id

if __name__ == '__main__':
    uvicorn.run(app=app,
                host='0.0.0.0',
                port=8080)