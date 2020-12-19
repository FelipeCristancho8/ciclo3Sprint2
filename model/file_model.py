from pydantic import BaseModel

class FileIn(BaseModel):
    id: str
    file_name : str
    file_type: str
    size : int
    file_img : str