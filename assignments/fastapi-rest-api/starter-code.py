from fastapi import FastAPI
from pydantic import BaseModel, Field

app = FastAPI(title="Task API")


class TaskCreate(BaseModel):
    title: str = Field(min_length=1, max_length=100)
    description: str = ""
    completed: bool = False


class TaskUpdate(BaseModel):
    title: str | None = Field(default=None, min_length=1, max_length=100)
    description: str | None = None
    completed: bool | None = None


class Task(TaskCreate):
    id: int


tasks: dict[int, Task] = {}
next_task_id = 1


@app.get("/")
def read_root():
    return {"message": "Welcome to the Task API. Visit /docs to explore it."}


# Add GET, POST, PATCH, and DELETE endpoints for tasks here.
