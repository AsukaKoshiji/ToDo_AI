from fastapi import APIRouter, HTTPException

from app.crud.todo import todo_crud
from app.schemas.todo import TodoCreate, TodoResponse, TodoUpdate

router = APIRouter(tags=["todos"])


@router.get("/", response_model=list[TodoResponse], summary="List all todos")
def read_todos() -> list[TodoResponse]:
    return todo_crud.get_all()


@router.post("/", response_model=TodoResponse, status_code=201, summary="Create a todo")
def create_todo(todo: TodoCreate) -> TodoResponse:
    return todo_crud.create(todo)


@router.get("/{todo_id}", response_model=TodoResponse, summary="Get a todo by ID")
def read_todo(todo_id: int) -> TodoResponse:
    todo = todo_crud.get_by_id(todo_id)
    if not todo:
        raise HTTPException(status_code=404, detail="Todo not found")
    return todo


@router.put("/{todo_id}", response_model=TodoResponse, summary="Update a todo")
def update_todo(todo_id: int, update: TodoUpdate) -> TodoResponse:
    todo = todo_crud.update(todo_id, update)
    if not todo:
        raise HTTPException(status_code=404, detail="Todo not found")
    return todo


@router.delete("/{todo_id}", status_code=204, summary="Delete a todo")
def delete_todo(todo_id: int) -> None:
    success = todo_crud.delete(todo_id)
    if not success:
        raise HTTPException(status_code=404, detail="Todo not found")
