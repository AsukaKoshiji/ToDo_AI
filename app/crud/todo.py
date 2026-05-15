# CRUD operations for Todo
from typing import List, Optional
from sqlalchemy.orm import Session

from app.models.todo import Todo
from app.schemas.todo import TodoCreate, TodoUpdate


def get_all(db: Session) -> List[Todo]:
    return db.query(Todo).all()


def get_by_id(db: Session, todo_id: int) -> Optional[Todo]:
    return db.query(Todo).filter(Todo.id == todo_id).first()


def create(db: Session, todo_data: TodoCreate) -> Todo:
    todo = Todo(
        title=todo_data.title,
        description=todo_data.description or "",
        completed=False
    )
    db.add(todo)
    db.commit()
    db.refresh(todo)
    return todo


def update(db: Session, todo_id: int, update_data: TodoUpdate) -> Optional[Todo]:
    todo = db.query(Todo).filter(Todo.id == todo_id).first()
    if not todo:
        return None
    update_dict = update_data.model_dump(exclude_unset=True)
    for key, value in update_dict.items():
        setattr(todo, key, value)
    db.commit()
    db.refresh(todo)
    return todo


def delete(db: Session, todo_id: int) -> bool:
    todo = db.query(Todo).filter(Todo.id == todo_id).first()
    if not todo:
        return False
    db.delete(todo)
    db.commit()
    return True
