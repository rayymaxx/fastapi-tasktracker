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
