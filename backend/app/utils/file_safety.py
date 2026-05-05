import os
from app.core.config import BASE_DIR

def get_user_base(username):
    user_dir = os.path.join(BASE_DIR, username)
    os.makedirs(user_dir, exist_ok = True)
    return user_dir

def get_safe_path(path, username=None):
    user_base = get_user_base(username) if username else BASE_DIR #storage/username
    full_path = os.path.abspath(os.path.join(user_base, path)) #storage/username + path(user input)
    
    #ensures user A can access only their own files and not user B's. since access directory = storage/username/*
    if not full_path.startswith(user_base): 
        raise Exception("Invalid Path :", BASE_DIR)
    
    return full_path