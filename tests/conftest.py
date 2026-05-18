import pytest

from app.db.database import SessionLocal
from app.models.todo import Todo


@pytest.fixture(autouse=True)
def clear_database():
    db = SessionLocal()

    db.query(Todo).delete()
    db.commit()

    db.close()