from fastapi import FastAPI

from app.api.routes.todo import router as todo_router

app = FastAPI()


app.include_router(todo_router)

from app.db.database import Base, engine

from app.models.todo import Todo

@app.get("/", summary="Root endpoint")
def read_root() -> dict[str, str]:
    return {"message": "hello"}

Base.metadata.create_all(bind=engine)
