from pydantic import BaseModel
from typing import Optional, Literal

class FileRequest(BaseModel):
    content : Optional[str] = None
    path : str
    operation : str
    mode : Literal["w", "a"] = "w"