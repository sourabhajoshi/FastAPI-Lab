from fastapi import FastAPI, Depends, status, HTTPException
from schemas.api import ApiResponse
from schemas.user import UserDetail
from routers.auth import auth_router
from routers.user import user_router

app = FastAPI()
app.include_router(auth_router)
app.include_router(user_router)

@app.get("/")
def root():
    print("Backend connected/called")
    return{
        "message": "backedn server working"
    }

# @app.get("/", response_model=ApiResponse)
# def home():
#     print("It's from root dir")
#     response = ApiResponse(message="First API APP", success=True, status="ok")
#     # return {
#     #     "message": "First API App",
#     #     "success": True,
#     #     "status": "ok"
#     # }
#     return response
    
# @app.get("/get-users")
# def get_users():
#     return{
#         "name": "Joshi", 
#         "age": 25,
#         "city": "Bidar"
#     }


# GET : Resuest

@app.get("/users")
def get_users():
    return{
        "message": "user created successfully"
    }
    
def get_token():
    print("getting token")
    return "jhcbedcvewucvewucvewiucbvewcbweih"
    
@app.post("/users", status_code=status.HTTP_201_CREATED)
def create_user(user: UserDetail, token=Depends(get_token)):
    if user.firstName == "abc":
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="user not allowed"
        )
    return{
        "message": "User created successfully",
        "user": user,
        "token": token
    }
    

