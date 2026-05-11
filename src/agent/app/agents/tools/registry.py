"""
Central registry for all agent tools.

This ensures:
- single source of truth
- easy scaling
- clean graph integration
"""

from tools.tool import create_file_tool, read_file_tool, create_folder_tool, delete_path_tool, list_files_tool, update_file_tool

tools = [
    create_file_tool, 
    read_file_tool, 
    create_folder_tool, 
    delete_path_tool, 
    list_files_tool,
    update_file_tool
]
