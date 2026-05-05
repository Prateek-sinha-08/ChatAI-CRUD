from sqlalchemy.orm import Session

from app.core.security import hash_password, verify_password, create_access_token
from app.models.user import User

def register_user(db: Session, username: str, password: str):
    
    existing_user = db.query(User).filter(User.username == username).first()
    
    if existing_user:
        return {"error: ": "User already exists"}
    
    hashed = hash_password(password)
    
    #new user object defined in models.user
    new_user = User(username=username, password=hashed)
    
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    
    return {"message :": "User registered!"}


def login_user(db: Session, username: str, password: str):
    
    user = db.query(User).filter(User.username == username).first()
    
    if not user:
        return {"error :": "User not found, register first"}
    
    if not verify_password(password, user.password):  #user.password comes from db
        return {"error :": "Invalid Password"}
    
    token = create_access_token({"sub": user.username})
    
    return {"access_token": token}
    
    
    
    
    