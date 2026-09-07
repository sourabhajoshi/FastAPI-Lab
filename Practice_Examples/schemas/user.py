from pydantic import BaseModel, Field

class UserDetail(BaseModel):
    firstName: str=Field(..., min_length=2, max_length=10)
    lastname: str
    city: str
    age: int
    isActive: bool=True