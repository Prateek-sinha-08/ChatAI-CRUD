import os
import shutil

from app.utils.file_safety import get_safe_path
from app.models.user import User

def list_files(path: str, user: User = None):
    safe_path = get_safe_path(path, user.username)

    if not os.path.exists(safe_path):
        raise Exception("Path not found!")
    
    if os.path.isdir(safe_path):
        items = os.listdir(safe_path)
        return {"files": items}

def create_file(path: str, content: str, user: User = None):
    safe_path = get_safe_path(path, user.username)
    
    os.makedirs(os.path.dirname(safe_path), exist_ok=True)
    
    with open(safe_path, "w") as f:
        f.write(content)
        
    return {"status": "file created", "path":safe_path}

def create_folder(path: str, content: str, user: User = None):
    safe_path = get_safe_path(path, user.username)
    
    os.makedirs(safe_path, exist_ok = True) 
    
    return {"status": "Folder created", "path ": safe_path}


def read_file(path: str, user: User = None):
    safe_path = get_safe_path(path, user.username)
    
    if not os.path.exists(safe_path):
        raise Exception("file not found")
    
    with open(safe_path, "r") as f:
        content = f.read()
        
    return {"content ": content}

def update_file(path: str, content: str, mode: str = "w", user: User = None):
    safe_path = get_safe_path(path, user.username)
    
    with open(safe_path, mode) as f:
        f.write(content)
        
    return {"status": f"file {'updated' if mode == 'w' else 'appended'}"}


def delete_path(path: str, user: User = None):
    safe_path = get_safe_path(path, user.username)

    if os.path.isdir(safe_path):
        shutil.rmtree(safe_path)
        
    else:
        os.remove(safe_path)
        
    return {"status":"deleted"}
    
