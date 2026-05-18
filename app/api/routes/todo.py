from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.db.database import get_db
from app.schemas.todo import TodoCreate, TodoUpdate, TodoOut
from app.crud.todo import (
    create_todo,
    get_todos,
    get_todo,
    update_todo,
    delete_todo
)

router = APIRouter(prefix="/todos", tags=["todos"])


# CREATE
@router.post("/", response_model=TodoOut)
def create(todo: TodoCreate, db: Session = Depends(get_db)):
    return create_todo(db, todo)


# READ ALL
@router.get("/", response_model=list[TodoOut])
def read_all(db: Session = Depends(get_db)):
    return get_todos(db)


# READ ONE
@router.get("/{todo_id}", response_model=TodoOut)
def read_one(todo_id: int, db: Session = Depends(get_db)):
    todo = get_todo(db, todo_id)
    if not todo:
        raise HTTPException(status_code=404, detail="Todo not found")
    return todo


# UPDATE
@router.put("/{todo_id}", response_model=TodoOut)
def update(todo_id: int, todo: TodoUpdate, db: Session = Depends(get_db)):
    updated = update_todo(db, todo_id, todo)
    if not updated:
        raise HTTPException(status_code=404, detail="Todo not found")
    return updated


# DELETE
@router.delete("/{todo_id}")
def delete(todo_id: int, db: Session = Depends(get_db)):
    deleted = delete_todo(db, todo_id)
    if not deleted:
        raise HTTPException(status_code=404, detail="Todo not found")
    return {"message": "deleted"}