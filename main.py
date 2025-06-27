from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from enum import Enum
from typing import Optional, List
from datetime import datetime

app = FastAPI()

# Enums for validation
class Status(str, Enum):
    pending = "pending"
    in_progress = "in_progress"
    completed = "completed"

class Priority(str, Enum):
    low = "low"
    medium = "medium"
    high = "high"

# Task Models
class TaskBase(BaseModel):
    title: str
    description: Optional[str] = None
    status: Status
    priority: Priority

class TaskCreate(TaskBase):
    pass

class TaskUpdate(TaskBase):
    pass

class Task(TaskBase):
    id: int
    created_at: datetime

# In-memory storage
tasks: List[Task] = []
task_id_counter = 1


@app.post("/tasks", response_model=Task, status_code=201)
def create_task(task: TaskCreate):
    global task_id_counter
    new_task = Task(
        id=task_id_counter,
        created_at=datetime.utcnow(),
        **task.dict()
    )
    tasks.append(new_task)
    task_id_counter += 1
    return new_task


@app.get("/tasks", response_model=List[Task])
def get_tasks(status: Optional[Status] = None, priority: Optional[Priority] = None):
    result = tasks
    if status:
        result = [task for task in result if task.status == status]
    if priority:
        result = [task for task in result if task.priority == priority]
    return result


