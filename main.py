from fastapi import FastAPI
from routers.todo import router as todo_router
from middleware.logger import LoggerMiddleware
from config.database import db
from datetime import datetime
import asyncio
from contextlib import asynccontextmanager

app = FastAPI()
app.add_middleware(LoggerMiddleware)
app.include_router(todo_router)

async def overdue_reminder_task():
    while True:
        now = datetime.utcnow()
        overdue_todos = await db.todos.find({"completed": False, "due_date": {"$lt": now}}).to_list(100)
        for todo in overdue_todos:
            print(f"Todo {todo['title']} is overdue!")
        await asyncio.sleep(86400)  # 24 hours; set lower for testing

@asynccontextmanager
async def lifespan(app: FastAPI):
    task = asyncio.create_task(overdue_reminder_task())
    yield
    task.cancel()

app = FastAPI(lifespan=lifespan)