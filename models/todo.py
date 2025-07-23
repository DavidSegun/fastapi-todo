from pydantic import BaseModel, Field
from typing import Optional
from datetime import datetime


class TodoModel(BaseModel):
    id: Optional[str] = Field(alias="_id")
    title: str
    due_date: datetime
    completed: bool = False
    created_at: datetime = Field(default_factory=datetime.utcnow)

    class Config:
        validate_by_name = True
        arbitrary_types_allowed = True 