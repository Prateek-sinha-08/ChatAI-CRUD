from sqlalchemy import Base, Column, Integer, String
class FileLog(Base):
    ___tablename___ = "file_logs"
    
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer)
    action = Column(String)
    path = Column(String)
    