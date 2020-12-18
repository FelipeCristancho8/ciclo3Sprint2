from fastapi import FastAPI, File, UploadFile, APIRouter, HTTPException
from typing import  Dict

from db.file_db import get_file, size_file_db, get_files, get_names_files, delete_file
from db.file_db import FileInDB, database_files
from model.file_model import FileIn

router = APIRouter()

import random


@router.get("/size")
async def sizeOfDictionary():
    file_in_db = size_file_db()
    return {"QuantityFiles": file_in_db}



@router.post("/files/")
async def create_file(file: bytes = File(...)):
    return {"file_size": len(file)}

#@router.post("/uploadfile/")
#async def create_upload_file(file: UploadFile = File(...)):    
#    sizeFile = await file.read()
#    return {"filename": file.filename,
#            "file_type" : file.content_type,
#            "size" : len(sizeFile)}

@router.post("/uploadfile/")
async def create_upload_file(file: UploadFile = File(...)):
    sizeFile = await file.read()
    newFile = "File"+ str(random.randint(11,10000))
    database_files.__setitem__(newFile,FileInDB(**{"file_name":file.filename,
                                                    "file_type":file.content_type,
                                                    "size":len(sizeFile)}))
      
    return {"Message": "File upload succesfully",
            "details": {
                "filename": file.filename,
                "file_type" : file.content_type,
                "size" : len(sizeFile)}
            }

@router.get("/file/{file_db}")
async def get_one_file(file_db: str):

    file_in_db = get_file(file_db)

    if file_in_db == None:
        raise HTTPException(status_code=404, detail="The file does not exists")

    file_out = FileIn(**file_in_db.dict())

    return file_out

@router.delete("/delete/{file_db}")
async def delete_one_file(file_db:str):
    file_in_db = get_file(file_db)

    if file_in_db == None:
        raise HTTPException(status_code=404, detail="The file does not exists")

    file_to_delete = delete_file(file_db)
    return {"Message" : "The file was deleted succesfully",
            "details" : file_to_delete}

@router.get("/list-files")
async def list_files():
    files_in_db = get_files()
    return files_in_db

@router.get("/list-name-files")
async def list_name_files():
    files = get_names_files()
    return files

