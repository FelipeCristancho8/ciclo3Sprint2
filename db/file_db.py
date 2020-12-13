from typing import  Dict
from pydantic import BaseModel

class FileInDB(BaseModel):
    file_name: str
    file_bd: str

database_files = Dict[str, FileInDB]

database_files = {
    "file1": FileInDB(**{"file_name":"archivo.txt",
                            "file_bd":"este es el archivo"}),

    "file2": FileInDB(**{"file_name":"archivo2.txt",
                            "file_bd":"este es el archivo 2"}),
}

def get_file(file_name: str):
    if file_name in database_files.keys():
        return database_files[file_name]
    else:
        return None

def size_file_db():
    return len(database_files)
