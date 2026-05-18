from langchain.tools import tool
from typing import Any


from src.agent.app.tools.file_tools import list_files, create_file, create_folder, read_file, update_file, delete_path

@tool
def list_files_tool(path: str, user: Any):
    """List files and folders at the specific path."""
    username = getattr(user, "username", user) if user is not None else None
    return list_files(path, username)

@tool
def create_file_tool(path: str, content: str, user: Any):
    """Create a file at the specific path with the given content."""
    username = getattr(user, "username", user) if user is not None else None
    return create_file(path, content, username)

@tool
def create_folder_tool(path: str, user: Any):
    """Create a folder at the specific path."""
    username = getattr(user, "username", user) if user is not None else None
    return create_folder(path, username)

@tool
def read_file_tool(path: str, user: Any):
    """Read the content of a file at the specific path."""
    username = getattr(user, "username", user) if user is not None else None
    return read_file(path, username)

@tool
def update_file_tool(path: str, content: str, mode: str = "w", user: Any = None):
    """Update the content of a file at the specific path. Mode can be 'w' for overwrite or 'a' for append."""
    username = getattr(user, "username", user) if user is not None else None
    return update_file(path, content, mode, username)

@tool
def delete_path_tool(path: str, user: Any = None):
    """Delete a file or folder at the specific path."""
    username = getattr(user, "username", user) if user is not None else None
    return delete_path(path, username)