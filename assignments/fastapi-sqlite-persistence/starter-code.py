import sqlite3
from contextlib import contextmanager
from pathlib import Path
from typing import Iterator

from fastapi import FastAPI
from pydantic import BaseModel, Field

app = FastAPI(title="Persistent Task API")
DATABASE_PATH = Path(__file__).with_name("tasks.db")


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


@contextmanager
def database_connection() -> Iterator[sqlite3.Connection]:
    connection = sqlite3.connect(DATABASE_PATH)
    connection.row_factory = sqlite3.Row
    try:
        yield connection
        connection.commit()
    finally:
        connection.close()


@app.on_event("startup")
def create_tasks_table() -> None:
    with database_connection() as connection:
        connection.execute(
            """
            CREATE TABLE IF NOT EXISTS tasks (
                id INTEGER PRIMARY KEY,
                title TEXT NOT NULL,
                description TEXT NOT NULL DEFAULT '',
                completed INTEGER NOT NULL DEFAULT 0
            )
            """
        )


@app.get("/")
def read_root():
    return {"message": "Welcome to the Persistent Task API. Visit /docs to explore it."}


# Add GET, POST, PATCH, and DELETE endpoints using database_connection().
# SQLite stores booleans as integers: use 0 or 1 in SQL and bool(value) in Python.
