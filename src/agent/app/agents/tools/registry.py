"""
Central registry for all agent tools.

This ensures:
- single source of truth
- easy scaling
- clean graph integration
"""

from tools.tool import create_file_tool, read_file_tool, create_folder_tool, delete_file_tool, list_files_tool

tools = [
    create_file_tool, 
    read_file_tool, 
    create_folder_tool, 
    delete_file_tool, 
    list_files_tool
]
