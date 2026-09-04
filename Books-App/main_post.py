from pydantic import BaseModel
from fastapi import FastAPI

app = FastAPI()

@app.post("/createuser")
def create_user(name:str, age:int):
    return {"name": name, "age": age}

class User(BaseModel):
    name: str
    age: int

@app.post("/create-user")
def create_user(users:User):
    return {
        "name": users.get("name"),
        "age": users.get("age")
    }