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
    newFile = "file"+ str(random.randint(11,10000))
    check_extension(file.filename)
    database_files.__setitem__(newFile,FileInDB(**{"id":newFile,
                                                    "file_name":file.filename,
                                                    "file_type":file.content_type,
                                                    "file_img" : check_extension(file.filename),
                                                    "size":len(sizeFile)}))
      
    return {"Message": "File upload succesfully",
            "details": {
                "id" : newFile,
                "filename": file.filename,
                "file_type" : file.content_type,
                "file_img" : check_extension(file.filename),
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

def check_extension(filename):
    if(".txt" in filename):
        return "https://i.ibb.co/YRtpwzJ/txt.png"
    elif(".rar" in filename):
        return "https://i.ibb.co/0mkMt3B/rar.png"
    elif(".png" in filename or ".jpg" in filename or ".JPG" in filename):
        return "https://i.ibb.co/B3HZ36D/imagen.png"
    elif(".doc" in filename or ".jpg" in filename):
        return "https://i.ibb.co/7YJ4ZTr/docs.png"
    elif(".xls" in filename or ".jpg" in filename):
        return "https://i.ibb.co/fkkvVyW/xls.png"
    else:
        return "https://i.ibb.co/kGPFswK/unknown.png"

