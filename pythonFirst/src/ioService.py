from fastapi import FastAPI, File, UploadFile
from typing import List
from modelUsers import userInfo
from uuid import uuid4
import csv
import codecs

app = FastAPI()

@app.get("/index")
async def root():
    return {"HELLO":"WORLD"}

@app.get("/users")
async def fetchUsers():
    return db;

@app.get("/upload/{inputValue}")
async def upload(inputValue):
    listUser = []
    with open("C:\Project\pythonFirst\src\sampledata.csv", newline='') as csvfile:
        csvReader = csv.reader(csvfile, delimiter=',')
        for row1,row2 in csvReader:
            if row2 == inputValue:
                dataDict = {}
                dataDict['user_id'] = row2
                dataDict['list_id'] = row1
                listUser.append(dataDict)
    with open("C:\Project\pythonFirst\src\download.csv",'w') as csvOutFile:
        fieldNames = ['user_id', 'list_id']
        writer = csv.DictWriter(csvOutFile,fieldnames=fieldNames)
        writer.writeheader()                 
        writer.writerows(listUser)                 
    return listUser


db: List[userInfo] = [
    userInfo(
        id=uuid4(),
        firstName="Jon",
        lastName="Cho"
        )
]