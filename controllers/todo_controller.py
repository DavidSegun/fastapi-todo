from models.todo import TodoModel
from motor.motor_asyncio import AsyncIOMotorDatabase
from fastapi import HTTPException
from datetime import datetime

async def create_todo_controller(db: AsyncIOMotorDatabase, todo: TodoModel):
    todo_dict = todo.dict(by_alias=True, exclude={"id"})
    todo_dict["created_at"] = datetime.utcnow()
    todo_dict["completed"] = False
    result = await db.todos.insert_one(todo_dict)
    todo_dict["_id"] = str(result.inserted_id)
    return TodoModel(**todo_dict)

async def get_all_todos_controller(db: AsyncIOMotorDatabase, overdue: bool = None):
    query = {}
    if overdue is not None:
        now = datetime.utcnow()
        if overdue:
            query = {"completed": False, "due_date": {"$lt": now}}
        else:
            query = {"completed": False, "due_date": {"$gte": now}}
    todos = await db.todos.find(query).to_list(100)
    for todo in todos:
        todo["_id"] = str(todo["_id"])
    return [TodoModel(**todo) for todo in todos]

async def mark_todo_done_controller(db: AsyncIOMotorDatabase, todo_id: str):
    result = await db.todos.update_one({"_id": todo_id}, {"$set": {"completed": True}})
    if result.modified_count == 0:
        raise HTTPException(status_code=404, detail="Todo not found")
    todo = await db.todos.find_one({"_id": todo_id})
    if todo:
        todo["_id"] = str(todo["_id"])
        return TodoModel(**todo)
    raise HTTPException(status_code=404, detail="Todo not found") 