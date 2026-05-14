from datetime import datetime
from typing import List, Optional

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI(
    title="ToDo API",
    description="A simple FastAPI-based ToDo application.",
    version="0.1.0",
)

class TodoBase(BaseModel):
    title: str
    description: Optional[str] = None
    completed: bool = False

class TodoCreate(TodoBase):
    pass

class TodoUpdate(BaseModel):
    title: Optional[str] = None
    description: Optional[str] = None
    completed: Optional[bool] = None

class Todo(TodoBase):
    id: int
    created_at: datetime

    class Config:
        orm_mode = True

todos: List[Todo] = []
next_id = 1


def get_todo(todo_id: int) -> Todo:
    for todo in todos:
        if todo.id == todo_id:
            return todo
    raise HTTPException(status_code=404, detail="ToDo not found")


@app.get("/todos", response_model=List[Todo])
def list_todos() -> List[Todo]:
    return todos


@app.get("/todos/{todo_id}", response_model=Todo)
def read_todo(todo_id: int) -> Todo:
    return get_todo(todo_id)


@app.post("/todos", response_model=Todo, status_code=201)
def create_todo(todo_in: TodoCreate) -> Todo:
    global next_id
    todo = Todo(
        id=next_id,
        title=todo_in.title,
        description=todo_in.description,
        completed=todo_in.completed,
        created_at=datetime.utcnow(),
    )
    todos.append(todo)
    next_id += 1
    return todo


@app.put("/todos/{todo_id}", response_model=Todo)
def update_todo(todo_id: int, update: TodoUpdate) -> Todo:
    todo = get_todo(todo_id)
    if update.title is not None:
        todo.title = update.title
    if update.description is not None:
        todo.description = update.description
    if update.completed is not None:
        todo.completed = update.completed
    return todo


@app.delete("/todos/{todo_id}", status_code=204)
def delete_todo(todo_id: int) -> None:
    todo = get_todo(todo_id)
    todos.remove(todo)
