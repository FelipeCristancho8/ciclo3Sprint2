from typing import  Dict
from pydantic import BaseModel

class FileInDB(BaseModel):
    file_name: str
    file_type: str
    size: int

database_files = Dict[str, FileInDB]

database_files = {
    "file1": FileInDB(**{"file_name":"archivo.rar",
                        "file_type":"compresed",
                        "size":235325}),

    "file2": FileInDB(**{"file_name":"archivo2.rar",
                         "file_type":"compresed",
                        "size":1234}),

    "file2": FileInDB(**{"file_name":"archivo2.txt",
                         "file_type":"txt",
                        "size":1234}),

    "file3": FileInDB(**{"file_name":"docuemento.docs",
                         "file_type":"docs",
                        "size":5436}),

    "file4": FileInDB(**{"file_name":"docuemnto.xls",
                         "file_type":"xls",
                        "size":98923}),

    "file5": FileInDB(**{"file_name":"archivo2.txt",
                         "file_type":"plain/txt",
                        "size":90238}),

    "file6": FileInDB(**{"file_name":"archivo2.txt",
                         "file_type":"compresed",
                        "size":4730239}),
    
    "file7": FileInDB(**{"file_name":"documento.txt",
                         "file_type":"txt",
                        "size":4730239}),
    
    "file8": FileInDB(**{"file_name":"archivos.rar",
                         "file_type":"compresed",
                        "size":4730239}),

    "file9": FileInDB(**{"file_name":"cuentas.xls",
                         "file_type":"xls",
                        "size":4730239}),

    "file10": FileInDB(**{"file_name":"juegos.rar",
                         "file_type":"compresed",
                        "size":4730239}),
}

def get_file(file_name: str):
    if file_name in database_files.keys():
        return database_files[file_name]
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
