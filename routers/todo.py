from fastapi import APIRouter, Depends, Query
from typing import List, Optional
from models.todo import TodoModel
from controllers.todo_controller import (
    create_todo_controller,
    get_all_todos_controller,
    mark_todo_done_controller
)
from config.database import get_database
from motor.motor_asyncio import AsyncIOMotorDatabase

router = APIRouter(prefix="/todos", tags=["todos"])

@router.post("/", response_model=TodoModel)
async def create_todo(todo: TodoModel, db: AsyncIOMotorDatabase = Depends(get_database)):
    return await create_todo_controller(db, todo)

@router.get("/", response_model=List[TodoModel])
async def get_todos(
    overdue: Optional[bool] = Query(None),
    db: AsyncIOMotorDatabase = Depends(get_database)
):
    return await get_all_todos_controller(db, overdue)

@router.patch("/{todo_id}", response_model=TodoModel)
async def mark_todo_done(todo_id: str, db: AsyncIOMotorDatabase = Depends(get_database)):
    return await mark_todo_done_controller(db, todo_id) 