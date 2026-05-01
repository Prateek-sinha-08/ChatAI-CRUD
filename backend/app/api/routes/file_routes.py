from fastapi import APIRouter
from pydantic import BaseModel


from app.services.file_services import handle_file_operations
from app.schemas.file_schema import FileRequest

router = APIRouter()

@router.post("/operate")
def operate_file(req: FileRequest):
    return handle_file_operations(req)