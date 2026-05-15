import pytest
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_read_todos_empty():
    response = client.get("/todos/")
    assert response.status_code == 200
    assert response.json() == []

def test_create_todo():
    todo_data = {"title": "Test Todo", "description": "Test Description", "completed": False}
    response = client.post("/todos/", json=todo_data)
    assert response.status_code == 201
    data = response.json()
    assert data["title"] == "Test Todo"
    assert data["description"] == "Test Description"
    assert data["completed"] == False
    assert "id" in data

def test_read_todo():
    # First create a todo
    todo_data = {"title": "Test Todo", "description": "Test Description", "completed": False}
    create_response = client.post("/todos/", json=todo_data)
    todo_id = create_response.json()["id"]

    response = client.get(f"/todos/{todo_id}")
    assert response.status_code == 200
    data = response.json()
    assert data["id"] == todo_id
    assert data["title"] == "Test Todo"

def test_update_todo():
    # First create a todo
    todo_data = {"title": "Test Todo", "description": "Test Description", "completed": False}
    create_response = client.post("/todos/", json=todo_data)
    todo_id = create_response.json()["id"]

    update_data = {"title": "Updated Todo", "completed": True}
    response = client.put(f"/todos/{todo_id}", json=update_data)
    assert response.status_code == 200
    data = response.json()
    assert data["title"] == "Updated Todo"
    assert data["completed"] == True

def test_delete_todo():
    # First create a todo
    todo_data = {"title": "Test Todo", "description": "Test Description", "completed": False}
    create_response = client.post("/todos/", json=todo_data)
    todo_id = create_response.json()["id"]

    response = client.delete(f"/todos/{todo_id}")
    assert response.status_code == 204

    # Verify it's deleted
    response = client.get(f"/todos/{todo_id}")
    assert response.status_code == 404

def test_read_todo_not_found():
    response = client.get("/todos/999")
    assert response.status_code == 404
    assert response.json()["detail"] == "Todo not found"

def test_update_todo_not_found():
    update_data = {"title": "Updated Todo"}
    response = client.put("/todos/999", json=update_data)
    assert response.status_code == 404
    assert response.json()["detail"] == "Todo not found"

def test_delete_todo_not_found():
    response = client.delete("/todos/999")
    assert response.status_code == 404
    assert response.json()["detail"] == "Todo not found"