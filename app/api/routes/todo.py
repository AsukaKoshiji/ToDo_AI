from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session

from app.crud.todo import get_all, get_by_id, create, update, delete
from app.schemas.todo import TodoCreate, TodoResponse, TodoUpdate
from app.db.database import get_db

router = APIRouter(tags=["todos"])


@router.get("/", response_model=list[TodoResponse], summary="List all todos")
def read_todos(db: Session = Depends(get_db)) -> list[TodoResponse]:
    return get_all(db)


@router.post("/", response_model=TodoResponse, status_code=201, summary="Create a todo")
def create_todo(todo: TodoCreate, db: Session = Depends(get_db)) -> TodoResponse:
    return create(db, todo)


@router.get("/{todo_id}", response_model=TodoResponse, summary="Get a todo by ID")
def read_todo(todo_id: int, db: Session = Depends(get_db)) -> TodoResponse:
    todo = get_by_id(db, todo_id)
    if not todo:
        raise HTTPException(status_code=404, detail="Todo not found")
    return todo


@router.put("/{todo_id}", response_model=TodoResponse, summary="Update a todo")
def update_todo(todo_id: int, update: TodoUpdate, db: Session = Depends(get_db)) -> TodoResponse:
    todo = update(db, todo_id, update)
    if not todo:
        raise HTTPException(status_code=404, detail="Todo not found")
    return todo


@router.delete("/{todo_id}", status_code=204, summary="Delete a todo")
def delete_todo(todo_id: int, db: Session = Depends(get_db)) -> None:
    success = delete(db, todo_id)
    if not success:
        raise HTTPException(status_code=404, detail="Todo not found")
