from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from src.agent.app.db.session import get_db
from src.agent.app.services.file_services import handle_file_operations
from src.agent.app.schemas.file_schema import FileRequest
from src.agent.app.deps.auth_dependency import get_current_user

router = APIRouter()

@router.post("/operate")
def operate_file(
    req: FileRequest,
    db: Session = Depends(get_db),
    user = Depends(get_current_user)
):
    return handle_file_operations(req, db, user)