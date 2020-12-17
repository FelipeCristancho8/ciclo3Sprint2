from pydantic import BaseModel

class FileIn(BaseModel):
    file_name : str
    file_type: str
    size : int