# 📘 Assignment: Persisting FastAPI Data with SQLite

## 🎯 Objective

Extend a task-management API so tasks are stored in a SQLite database instead of only in memory. The API should keep working across server restarts while preserving its validation and CRUD behavior.

## 📝 Tasks

### 🛠️ Create the Tasks Database

#### Description
Inspect the provided starter code and use its database setup to create a `tasks` table. SQLite is included with Python, so no database server or extra database package is needed.

#### Requirements
Completed program should:

- Create a `tasks.db` file beside `main.py`
- Create a `tasks` table with an integer primary key, title, description, and completed status
- Create the table automatically when the API starts, without deleting existing task data

### 🛠️ Connect Read and Create Endpoints

#### Description
Replace in-memory task storage with SQL queries. Implement endpoints to list tasks, retrieve one task, and create a new task.

#### Requirements
Completed API should:

- Return rows from `GET /tasks` and one matching row from `GET /tasks/{task_id}`
- Return HTTP 404 when the requested task ID does not exist
- Insert tasks from `POST /tasks` and return the saved task with HTTP 201
- Use parameterized SQL queries rather than building SQL with string formatting

### 🛠️ Update, Delete, and Verify Persistence

#### Description
Finish the database-backed CRUD API and test that stored tasks remain available after restarting the server.

#### Requirements
Completed API should:

- Update only the fields supplied to `PATCH /tasks/{task_id}`
- Delete a task with `DELETE /tasks/{task_id}`
- Return HTTP 404 when an update or delete targets an unknown ID
- Keep task titles between 1 and 100 characters, as in the FastAPI assignment
- Demonstrate creating a task, restarting the server, and retrieving that task again

## 🚀 Getting Started

1. Install Python 3.10 or newer.
2. Install FastAPI and Uvicorn with `pip install "fastapi[standard]"`.
3. Open `starter-code.py`, implement the database-backed endpoints, and save your work as `main.py`.
4. Start the API with `uvicorn main:app --reload`.
5. Open `http://127.0.0.1:8000/docs` to test the API.

The `sqlite3` module is part of Python’s standard library. The database file is created beside `main.py`; do not delete it when restarting the server.
