import os
from app.core.config import BASE_DIR


def get_safe_path(path):
    full_path = os.path.abspath(os.path.join(BASE_DIR, path)) #storage + path(user input)
    
    if not full_path.startswith(BASE_DIR):
        raise Exception("Invalid Path :", BASE_DIR)
    
    return full_path