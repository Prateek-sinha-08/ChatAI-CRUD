from langchain.tools import tool
from typing import Any


from src.agent.app.models.user import User
from src.agent.app.tools.file_tools import list_files, create_file, create_folder, read_file, update_file, delete_path

@tool
def list_files_tool(path: str, user: Any):
    """List files and folders at the specific path."""
    return list_files(path, user)

@tool
def create_file_tool(path: str, content: str, user: Any):
    """Create a file at the specific path with the given content."""
    return create_file(path, content, user)

@tool
def create_folder_tool(path: str, user: Any):
    """Create a folder at the specific path."""
    return create_folder(path, user)

@tool
def read_file_tool(path: str, user: Any):
    """Read the content of a file at the specific path."""
    return read_file(path, user)

@tool
def update_file_tool(path: str, content: str, mode: str = "w", user: Any = None):
    """Update the content of a file at the specific path. Mode can be 'w' for overwrite or 'a' for append."""
    return update_file(path, content, mode, user)

@tool
def delete_path_tool(path: str, user: Any = None):
    """Delete a file or folder at the specific path."""
    return delete_path(path, user)