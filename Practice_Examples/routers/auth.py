# all apis of authentication

from fastapi import APIRouter

auth_router=APIRouter(prefix="/auth")

@auth_router.post("/login")
def login():
    print("login api called")
    return{
        "message": "login API called"
    }
    

@auth_router.post("/register")
def register():
    print("register API called")
    return{
        "message": "Register API called"
    }
    
@auth_router.post("/logout")
def logout():
    print("logout API called")
    return{
        "message": "Logged out "
    }