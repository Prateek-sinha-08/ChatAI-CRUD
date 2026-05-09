from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.sql import func

from app.db.base import Base


class FileLog(Base):
    __tablename__ = "file_logs"
    
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer)
    action = Column(String)
    path = Column(String)
    time = Column(DateTime(timezone=True), default=func.now())