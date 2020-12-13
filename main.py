from fastapi import FastAPI, File, UploadFile
from routes import userRoutes 
from db.file_db import FileInDB
from db.file_db import get_file, size_file_db
from model.file_model import FileIn
from fastapi import FastAPI, HTTPException

app = FastAPI()

app.include_router(userRoutes.router)

@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.post("/files/")
async def create_file(file: bytes = File(...)):
    return {"file_size": len(file)}


@app.post("/uploadfile/")
async def create_upload_file(file: UploadFile = File(...)):
    return {"filename": file.filename}

@app.get("/file/{file_db}")
async def get_balance(file_db: str):

    file_in_db = get_file(file_db)

    if file_in_db == None:
        raise HTTPException(status_code=404, detail="El archivo no existe")

    file_out = FileIn(**file_in_db.dict())

    return file_out

@app.get("/size")
async def get_files():

    file_in_db = size_file_db()

    return {"cantidad de registros": file_in_db}