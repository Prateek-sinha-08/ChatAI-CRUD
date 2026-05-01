#these services are the Business Logic that handles the tools etc

from fastapi import HTTPException


from app.tools import file_tools
from app.schemas.file_schema import FileRequest

def handle_file_operations(req: FileRequest):
    
    if req.operation == "create_file":
        return file_tools.create_file(req.path)
    
    if req.operation == "create_folder":
        return file_tools.create_folder(req.path)
    
    elif req.operation == "read":
        return file_tools.read_file(req.path)
    
    elif req.operation == "update":
        return file_tools.update_file(req.path, req.content, req.mode)
    
    elif req.operation == "delete":
        return file_tools.delete_path(req.path)
    
    else:
        raise HTTPException(status_code=400, detail="Invalid Operation")
    
