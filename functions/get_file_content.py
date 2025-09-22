import os
from .config import *

def get_file_content(working_directory, file_path):
    full_path = os.path.join(working_directory, file_path)

    try:
        target = os.path.realpath(full_path)
        root = os.path.realpath(working_directory)
        
        if os.path.commonpath([target, root]) != root:
            return f'Error: Cannot read "{file_path}" as it is outside the permitted working directory'
        if not os.path.isfile(target):
            return f'Error: File not found or is not a regular file: "{file_path}"'
        
        with open(target, "r") as f:
            file_content_string = f.read()
            if len(file_content_string) > MAX_CHARS:
                return file_content_string[:MAX_CHARS] + f'[...File "{file_path}" truncated at 10000 characters]'
            return file_content_string
        
    except Exception as e:
        return f'Error reading file "{file_path}": {e}'
        
    
