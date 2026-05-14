from typing import Optional

from pydantic import BaseModel


class TodoBase(BaseModel):
    title: str
    description: Optional[str] = None


class TodoCreate(TodoBase):
    pass


class TodoResponse(TodoBase):
    id: int
    completed: bool = False

    class Config:
        orm_mode = True
