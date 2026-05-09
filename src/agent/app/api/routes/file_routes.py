from fastapi import APIRouter, Depends
from app.db.session import get_db
from sqlalchemy.orm import Session


from app.services.file_services import handle_file_operations
from app.schemas.file_schema import FileRequest
from app.deps.auth_dependency import get_current_user

router = APIRouter()

@router.post("/operate")
def operate_file(
    req: FileRequest,
    db: Session = Depends(get_db),
    user = Depends(get_current_user)
):
    return handle_file_operations(req, db, user)