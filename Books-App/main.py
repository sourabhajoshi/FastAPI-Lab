from fastapi import FastAPI

app = FastAPI()

# Root endpoint
@app.get("/")
def home():
    return {"message": "Welcome to fast API app"}

# about route
@app.get("/about")
def about():
    return {"message": "This is about route of fast API app"}   

# user route
@app.get("/users")
def users():
    return {"users": ["user1", "user2", "user3"]}

# dynamic route
@app.get("/users/{user_id}")
def get_user(user_id: int):
    return {"user_id": user_id, "name": f"user{user_id}"}

# dynamic route bassed on data type
@app.get("/items/{item_id}")
def get_item(item_id: int):
    return {"item_id": item_id, "name": f"item{item_id}"}

# Optional parameter
@app.get("/items/")
def get_items(skip: int = 0, limit: int = 10):
    return {"skip": skip, "limit": limit, "items": [f"item{i}" for i in range(skip, skip + limit)]}

