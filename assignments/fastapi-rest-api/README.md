# 📘 Assignment: Building REST APIs with FastAPI

## 🎯 Objective

Build a small REST API for managing tasks using FastAPI. You will define data models, create endpoints for the main HTTP methods, validate input, and return appropriate responses.

## 📝 Tasks

### 🛠️ Read Tasks from the API

#### Description
Use the provided starter code to create read endpoints for a task list. Each task has an integer `id`, a `title`, a `description`, and a `completed` status.

#### Requirements
Completed API should:

- Run locally with `uvicorn main:app --reload`
- Return all tasks from `GET /tasks`
- Return one task from `GET /tasks/{task_id}` and respond with HTTP 404 when its ID does not exist
- Show the interactive API documentation at `/docs`

### 🛠️ Create and Validate Tasks

#### Description
Add an endpoint that lets a client create a task. Use a Pydantic model to validate the request body.

#### Requirements
Completed API should:

- Accept `POST /tasks` with a title and optional description and completed status
- Require a title between 1 and 100 characters
- Assign a unique integer ID to each new task
- Return the created task with HTTP 201

### 🛠️ Update and Delete Tasks

#### Description
Complete the API by allowing clients to update a task’s fields or delete a task.

#### Requirements
Completed API should:

- Accept `PATCH /tasks/{task_id}` to update one or more task fields
- Accept `DELETE /tasks/{task_id}` to remove a task
- Respond with HTTP 404 when an update or delete targets an unknown ID
- Demonstrate the endpoints using `/docs` or an HTTP client, including a missing-ID request

## 🚀 Getting Started

1. Install Python 3.10 or newer.
2. Install FastAPI and Uvicorn with `pip install "fastapi[standard]"`.
3. Open `starter-code.py` and implement the endpoints described above.
4. Save your completed file as `main.py`, then start the API with `uvicorn main:app --reload`.
5. Open `http://127.0.0.1:8000/docs` to try your endpoints.

The task data can be stored in a Python list or dictionary while the server is running. It will reset when the server restarts.
