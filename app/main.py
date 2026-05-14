from fastapi import FastAPI

from app.api.routes.todo import router as todo_router

app = FastAPI(title="ToDo API", version="0.1.0")

app.include_router(todo_router, prefix="/todos", tags=["todos"])


@app.get("/", summary="Root endpoint")
def read_root() -> dict[str, str]:
    return {"message": "hello"}