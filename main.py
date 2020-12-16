from fastapi import FastAPI, File, UploadFile
from fastapi.middleware.cors import CORSMiddleware

from routes import userRoutes 
from routes import fileRoutes
from db.file_db import FileInDB
from db.file_db import get_file, size_file_db
from model.file_model import FileIn


app = FastAPI()

origins = ['*']

app.add_middleware(
    CORSMiddleware, allow_origins=origins,
    allow_credentials=True, allow_methods=["*"], allow_headers=["*"],
)

app.include_router(userRoutes.router)
app.include_router(fileRoutes.router)

@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/size")
async def get_files():

    file_in_db = size_file_db()

    return {"cantidad de registros": file_in_db}