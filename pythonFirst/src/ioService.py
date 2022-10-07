from fastapi import FastAPI
from typing import List
from modelUser import userInfo
from uuid import uuid4

app = FastAPI()

db: List[userInfo] = [
    userInfo(
        id=uuid4(),
        firstName="Jon",
        lastName="Cho"
        )
]

@app.get("/index")
async def root():
    return {"HELLO":"WORLD"}

@app.get("/api/users")
async def fetchUsers():
    return db;