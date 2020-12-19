from typing import  Dict
from pydantic import BaseModel

class FileInDB(BaseModel):
    id: str
    file_name: str
    file_type: str
    size: int
    file_img: str

database_files = Dict[str, FileInDB]

database_files = {
    "file1": FileInDB(**{"id":"file1",
                        "file_name":"archivo.rar",
                        "file_type":"compresed",
                        "file_img":"https://i.ibb.co/0mkMt3B/rar.png",
                        "size":235325}),

    "file2": FileInDB(**{"id":"file2",
                        "file_name":"archivo2.txt",
                         "file_type":"txt",
                         "file_img":"https://i.ibb.co/YRtpwzJ/txt.png",
                        "size":1234}),

    "file3": FileInDB(**{"id":"file3",
                        "file_name":"docuemento.docs",
                         "file_type":"docs",
                         "file_img":"https://i.ibb.co/7YJ4ZTr/docs.png",
                        "size":5436}),

    "file4": FileInDB(**{"id":"file4",
                        "file_name":"docuemnto.xls",
                         "file_type":"xls",
                         "file_img":"https://i.ibb.co/fkkvVyW/xls.png",
                        "size":98923}),

    "file5": FileInDB(**{"id":"file5",
                        "file_name":"archivo2.txt",
                         "file_type":"plain/txt",
                         "file_img":"https://i.ibb.co/YRtpwzJ/txt.png",
                        "size":90238}),

    "file6": FileInDB(**{"id":"file6",
                        "file_name":"archivo2.txt",
                         "file_type":"compresed",
                         "file_img":"https://i.ibb.co/YRtpwzJ/txt.png",
                        "size":4730239}),
    
    "file7": FileInDB(**{"id":"file7",
                        "file_name":"documento.txt",
                         "file_type":"txt",
                         "file_img":"https://i.ibb.co/YRtpwzJ/txt.png",
                        "size":4730239}),
    
    "file8": FileInDB(**{"id":"file8",
                        "file_name":"archivos.rar",
                         "file_type":"compresed",
                         "file_img":"https://i.ibb.co/0mkMt3B/rar.png",
                        "size":4730239}),

    "file9": FileInDB(**{"id":"file9",
                        "file_name":"cuentas.xls",
                         "file_type":"xls",
                         "file_img":"https://i.ibb.co/fkkvVyW/xls.png",
                        "size":4730239}),

    "file10": FileInDB(**{"id":"file10",
                        "file_name":"juegos.rar",
                         "file_type":"compresed",
                         "file_img":"https://i.ibb.co/0mkMt3B/rar.png",
                        "size":4730239}),
}

def get_file(file_name: str):
    if file_name in database_files.keys():
        return database_files[file_name]
    else:
        return None
        
def delete_file(file_name: str):
    if file_name in database_files.keys():
        file_deleted = database_files[file_name]
        database_files.pop(file_name)
        return file_deleted
    else:
        return None

def size_file_db():
    return len(database_files)

def get_files():
    files = []
    for t in database_files.keys():
        archivo = database_files[t]
        files.append(archivo)
    return files

def get_names_files():
    return database_files
