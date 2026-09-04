from pydantic import BaseModel
from fastapi import FastAPI

app = FastAPI()

# class User(BaseModel):
#     user: str
#     age: int
#     emai: str
#     is_active: bool
    
# @app.post("/create-user")
# def create_users(user: User):
#     return{
#         "message" : "User created successfully",
#         "user" : user
#     }
    
    
 # Nested data/models   
class Address(BaseModel):
    city: str
    state: str
    country: str

class Person(BaseModel):
    name: str
    age: int
    address: Address
    
@app.post("/create-new-user")
def create_user(user: Person):
    return {
        "message": "User retrieved successfully",
        "user": Person
    }   