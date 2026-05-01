import os
import shutil

from app.utils.file_safetly import get_safe_path


def create_file(path: str):
    safe_path = get_safe_path(path)
    
    os.makedirs(os.path.dirname(safe_path), exist_ok=True)
    
    with open(safe_path, "w") as f:
        f.write("")
        
    return {"status": "file created", "path":safe_path}

def create_folder(path: str):
    safe_path = get_safe_path(path)
    
    os.mkdir(safe_path, exist_ok = True) 
    
    return {"status": "Folder created", "path ": safe_path}


def read_file(path: str):
    safe_path = get_safe_path(path)
    
    if not os.path.exists(safe_path):
        raise Exception("file not found")
    
    with open(safe_path, "r") as f:
        content = f.read()
        
    return {"content ": content}

def update_file(path: str, content: str, mode: str = "w"):
    safe_path = get_safe_path(path)
    
    with open(safe_path, mode) as f:
        f.write(content)
        
    return {"status": f"file {'updated' if mode == 'w' else 'appended'}"}


def delete_path(path: str):
    safe_path = get_safe_path(path)
    
    if os.path.isdir(safe_path):
        shutil.rmtree(safe_path)
        
    else:
        os.remove(safe_path)
        
    return {"status":"deleted"}
    
