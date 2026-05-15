# CRUD operations for Todo
from typing import List, Optional

from app.models.todo import Todo
from app.schemas.todo import TodoCreate, TodoUpdate


class TodoCRUD:
    def __init__(self):
        self.todos: List[Todo] = []
        self.next_id = 1

    def get_all(self) -> List[Todo]:
        return self.todos

    def get_by_id(self, todo_id: int) -> Optional[Todo]:
        for todo in self.todos:
            if todo.id == todo_id:
                return todo
        return None

    def create(self, todo_data: TodoCreate) -> Todo:
        todo = Todo(
            id=self.next_id,
            title=todo_data.title,
            description=todo_data.description or "",
            completed=False
        )
        self.todos.append(todo)
        self.next_id += 1
        return todo

    def update(self, todo_id: int, update_data: TodoUpdate) -> Optional[Todo]:
        todo = self.get_by_id(todo_id)
        if not todo:
            return None
        if update_data.title is not None:
            todo.title = update_data.title
        if update_data.description is not None:
            todo.description = update_data.description
        if update_data.completed is not None:
            todo.completed = update_data.completed
        return todo

    def delete(self, todo_id: int) -> bool:
        todo = self.get_by_id(todo_id)
        if not todo:
            return False
        self.todos.remove(todo)
        return True


todo_crud = TodoCRUD()
