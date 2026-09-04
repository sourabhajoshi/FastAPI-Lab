# CRUD Features for Todo App using FastAPI
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()
todos = []

class Todo(BaseModel):
    id: int
    title: str
    completed: bool
    
    
# Create a new todo
@app.post("/todos")
def create_todo(todo: Todo):
    todos.append(todo)
    return {"message": "Todo created successfully", "todo": todo}   

# get todo
@app.get("/todos")
def get_todos():
    return {"todos": todos}

@app.get("todos/{todo_id}")
def get_todo(todo_id: int):
    for todo in todos:
        if todo.id == todo_id:
            return {"todo": todo}
    return {"message": "Todo not found"}