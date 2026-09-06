from fastapi import FastAPI
from schemas.api import ApiResponse

app = FastAPI()

@app.get("/", response_model=ApiResponse)
def home():
    print("It's from root dir")
    response = ApiResponse(message="First API APP", success=True, status="ok")
    # return {
    #     "message": "First API App",
    #     "success": True,
    #     "status": "ok"
    # }
    return response
    
@app.get("/get-users")
def get_users():
    return{
        "name": "Joshi", 
        "age": 25,
        "city": "Bidar"
    }