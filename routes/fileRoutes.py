from fastapi import FastAPI, File, UploadFile, APIRouter, HTTPException

from db.file_db import get_file, size_file_db, get_files
from db.file_db import FileInDB
from model.file_model import FileIn

router = APIRouter()


@router.post("/files/")
async def create_file(file: bytes = File(...)):
    return {"file_size": len(file)}

@router.post("/uploadfile/")
async def create_upload_file(file: UploadFile = File(...)):    
    sizeFile = await file.read()
    return {"filename": file.filename,
            "type" : file.content_type,
            "size" : len(sizeFile)}

@router.get("/file/{file_db}")
async def get_one_file(file_db: str):

    file_in_db = get_file(file_db)

    if file_in_db == None:
        raise HTTPException(status_code=404, detail="El archivo no existe")

    file_out = FileIn(**file_in_db.dict())

    return file_out

@router.get("/list-files")
async def list_files():
    files_in_db = get_files()
    return files_in_db