from typing import List
from fastapi import APIRouter, Depends

from sqlalchemy.ext.asyncio import AsyncSession

import api.schemas.task as task_schema
import api.cruds.task as task_crud
from api.db import get_db

router = APIRouter()

@router.get("/tasks", response_model=List[task_schema.Task])
async def list_tasks(db: AsyncSession = Depends(get_db)):
  return await task_crud.get_tasks_with_done(db)

@router.post("/tasks")
async def create_task(task_body: task_schema.TaskCreate, db: AsyncSession = Depends(get_db)):
  return await task_crud.create_task(db, task_body)

@router.put("/tasks/{task_id}")
async def update_task(task_id: int, task_body: task_schema.TaskCreate):
  return task_schema.TaskCreateResponse(id=task_id, **task_body.dict())

@router.delete("/tasks/{task_id}")
async def delete_task(task_id: int):
  return
