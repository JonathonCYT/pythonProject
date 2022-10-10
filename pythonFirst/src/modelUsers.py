from typing import Optional
from uuid import UUID, uuid4
from pydantic import BaseModel
from fastapi import FastAPI

app = FastAPI()

class userInfo(BaseModel):
    id: Optional[UUID] = uuid4
    firstName: str
    lastName: str
    
class userOutput(BaseModel):
    id: str
    firstName: str
    lastName: str    