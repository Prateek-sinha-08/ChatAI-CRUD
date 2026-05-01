from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session


from app.services.auth_services import login_user, register_user
from app.schemas.auth_schema import UserLogin, UserRegister
from app.db.session import get_db


router = APIRouter()

@router.post("/register")
def register(req: UserRegister, db: Session = Depends(get_db)):
    return register_user(db, req.username, req.password)

@router.post("/login")
def login(req: UserLogin, db: Session = Depends(get_db)):
    return login_user(db, req.username, req.password)


