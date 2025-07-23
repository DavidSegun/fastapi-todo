from motor.motor_asyncio import AsyncIOMotorClient
from fastapi import Request, Depends
import os

MONGODB_URL = os.getenv("MONGODB_URL", "mongodb+srv://test:nvzUUaOey2ADraeZ@cluster0.zkd0yrw.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
MONGO_DB_NAME = os.getenv("MONGO_DB_NAME", "todo_db")

client = AsyncIOMotorClient(MONGODB_URL)
db = client[MONGO_DB_NAME]

def get_database(request: Request):
    return db 