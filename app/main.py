from fastapi import FastAPI
from app.api.routers import todo

from app.api.routes.todo import router as todo_router

app = FastAPI(
    title="ToDo AI API",
    description="""
AI-Native 開発を前提に構築した ToDo API。

## Features

- ToDo CRUD
- MySQL
- SQLAlchemy
- Alembic Migration
- pytest
- Docker Support
""",
    version="1.0.0",
)

app.include_router(todo.router, prefix="/todos", tags=["Todos"])

app.include_router(todo_router, prefix="/todos", tags=["todos"])

from app.db.database import Base, engine

from app.models.todo import Todo

@app.get("/", summary="Root endpoint")
def read_root() -> dict[str, str]:
    return {"message": "hello"}

Base.metadata.create_all(bind=engine)
