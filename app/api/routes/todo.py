from fastapi import APIRouter

from app.schemas.todo import TodoCreate, TodoResponse

router = APIRouter(tags=["todos"])


@router.get("/", response_model=list[TodoResponse], summary="List all todos")
def read_todos() -> list[TodoResponse]:
    return []


@router.post("/", response_model=TodoResponse, summary="Create a todo")
def create_todo(todo: TodoCreate) -> TodoResponse:
    return TodoResponse(id=0, title=todo.title, description=todo.description or "", completed=False)
