#these services are the Business Logic that handles the tools etc

from fastapi import HTTPException
from datetime import datetime, timezone
from sqlalchemy.orm import Session

from app.tools import file_tools
from app.models.user import User
from app.models.file_log import FileLog
from app.schemas.file_schema import FileRequest

def handle_file_operations(req: FileRequest, db: Session, user: User):

    if req.operation == "list":
        res = file_tools.list_files(req.path, user)

    elif req.operation == "create_file":
        res = file_tools.create_file(req.path, req.content, user)
    
    elif req.operation == "create_folder":
        res =file_tools.create_folder(req.path, req.content, user)
    
    elif req.operation == "read":
        res =file_tools.read_file(req.path, user)
    
    elif req.operation == "update":
        res = file_tools.update_file(req.path, req.content, req.mode, user)
    
    elif req.operation == "delete":
        res = file_tools.delete_path(req.path, user)
    
    else:
        raise HTTPException(status_code=400, detail="Invalid Operation")
    
    new_log = FileLog(
        user_id = user.id,
        action = req.operation  ,
        path = req.path,
        time = datetime.now(timezone.utc)
        )
    
    db.add(new_log) #add the log to the session, but it is not yet committed to the database. The commit() method is called later to save the changes to the database.  
    db.commit()

    return res
    
