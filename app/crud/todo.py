from sqlalchemy.orm import Session
from app.models.todo import Todo
from app.schemas.todo import TodoCreate, TodoUpdate

# CREATE
def create_todo(db: Session, todo: TodoCreate):
    db_todo = Todo(
        title=todo.title,
        description=todo.description,
        completed=False
    )
    db.add(db_todo)
    db.commit()
    db.refresh(db_todo)
    return db_todo


# READ ALL
def get_todos(db: Session):
    return db.query(Todo).all()


# READ ONE
def get_todo(db: Session, todo_id: int):
    return db.query(Todo).filter(Todo.id == todo_id).first()


# UPDATE
def update_todo(db: Session, todo_id: int, todo: TodoUpdate):
    db_todo = get_todo(db, todo_id)
    if not db_todo:
        return None

    if todo.title is not None:
        db_todo.title = todo.title
    if todo.description is not None:
        db_todo.description = todo.description
    if todo.completed is not None:
        db_todo.completed = todo.completed

    db.commit()
    db.refresh(db_todo)
    return db_todo


# DELETE
def delete_todo(db: Session, todo_id: int):
    db_todo = get_todo(db, todo_id)
    if not db_todo:
        return None

    db.delete(db_todo)
    db.commit()
    return db_todo