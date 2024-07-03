from fastapi import FastAPI, HTTPException, Depends, status
from fastapi.security import HTTPBasic, HTTPBasicCredentials
from typing import List
from uuid import uuid4

from models import TodoItem
from schemas import TodoCreate, TodoUpdate

app = FastAPI()

# In-memory list to store todo items
todos = []

# Basic Authentication
security = HTTPBasic()

# Function to verify credentials
def get_current_username(credentials: HTTPBasicCredentials = Depends(security)):
    correct_username = "admin"
    correct_password = "password"
    if credentials.username != correct_username or credentials.password != correct_password:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid credentials",
            headers={"WWW-Authenticate": "Basic"},
        )
    return credentials.username

# Create a Todo Item
@app.post("/todos/", response_model=TodoItem)
def create_todo(todo: TodoCreate, username: str = Depends(get_current_username)):
    new_todo = TodoItem(id=str(uuid4()), title=todo.title, description=todo.description)
    todos.append(new_todo)
    return new_todo

# Read All Todo Items with pagination
@app.get("/todos/", response_model=List[TodoItem])
def read_todos(skip: int = 0, limit: int = 10, username: str = Depends(get_current_username)):
    return todos[skip: skip + limit]

# Read a Single Todo Item
@app.get("/todos/{todo_id}", response_model = TodoItem)
def read_todo(todo_id: str, username: str = Depends(get_current_username)):
    for todo in todos:
        if todo.id == todo_id:
            return todo
    raise HTTPException(status_code=404, detail="Todo item not found")

# Update a Todo Item
@app.put("/todos/{todo_id}", response_model=TodoItem)
def update_todo(todo_id: str, todo_update: TodoUpdate, username: str = Depends(get_current_username)):
    for todo in todos:
        if todo.id == todo_id:
            todo.title = todo_update.title
            todo.description = todo_update.description
            todo.completed = todo_update.completed
            return todo
    raise HTTPException(status_code=404, detail="Todo item not found")

# Delete a Todo Item
@app.delete("/todos/{todo_id}", response_model=dict)
def delete_todo(todo_id: str, username: str = Depends(get_current_username)):
    for index, todo in enumerate(todos):
        if todo.id == todo_id:
            todos.pop(index)
            return {"detail": "Todo item deleted"}
    raise HTTPException(status_code=404, detail="Todo item not found")
