from pydantic import BaseModel

class ExpenseRequest(BaseModel):
    title: str
    description: str
    
    
class ExpenseResponse(BaseModel):
    title: str
    description: str
    created_date: str
    
    