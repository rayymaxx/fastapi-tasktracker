# Task Manager API

This is a simple task manager backend API built with FastAPI for freelancers.

## 🔧 Features

- Create, read, update, and delete tasks
- Filters for status and priority
- Swagger UI for interactive testing

## Live Demo
https://fastapi-tasktracker.vercel.app/

## 📘 Docs (Swagger UI): 
https://fastapi-tasktracker.vercel.app/docs

## 🚀 Run Locally

1. Clone the repo:
    ```
    git clone https://github.com/rayymaxx/fastapi-tasktracker.git
    cd fastapi-tasktracker
    ```

2. Create a virtual environment:
    ```
    python -m venv venv
    venv\Scripts\activate
    ```

3. Install dependencies:
    ```
    pip install -r requirements.txt
    ```

4. Run the server:
    ```
    uvicorn main:app --reload
    ```

5. Open `http://localhost:8000/docs` in your browser.

## 🔎 Endpoints

| Method | Endpoint       | Description         |
|--------|----------------|---------------------|
| GET    | `/tasks`       | List all tasks      |
| POST   | `/tasks`       | Create a new task   |
| PUT    | `/tasks/{id}`  | Update a task       |
| DELETE | `/tasks/{id}`  | Delete a task       |

## 📝 Example JSON
```json
{
  "title": "Write blog post",
  "description": "About FastAPI project",
  "status": "pending",
  "priority": "high"
}

