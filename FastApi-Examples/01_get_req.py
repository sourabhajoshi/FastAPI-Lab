from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

# GET- Operations
@app.get("/users")
def get_users():
    return{
        "message": "Users list",
        "status": "ok"
    }
    
@app.get("/users/search")
def search_user(first_name:str="", last_name:str=""):
    print(first_name, last_name)
    return{
        "user": []
    }
    

@app.get("/books")
def get_users():
    return ["system design", "control systems"]



# POST - Operations
@app.post("/users")
def create_user():
    return{
        "message": "users created",
        "status": "ok",
        "success": True
    }
    
class Books(BaseModel):
    title: str
    author: str
    
# POST - Operations
@app.post("/books/")
def create_book(book:Books):
    return{
        "message": "users created",
        "status": "ok",
        "success": True,
        "book": book
    }
    
    
# PUT - Operations
@app.put("/users/{user_id}")
def updated_user(user_id: int):
    return{
        "message": "user updated"
    }
    
@app.put("/books/{book_id}/name/{book_name}")
def updated_book(book_id: int, book_name: str):
    return{
        "message": "book updated",
        "book_id": book_id,
        "book_name": book_name
    }
    
