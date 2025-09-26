import os
from google.genai import types

def write_file(working_directory, file_path, content):
    full_path = os.path.join(working_directory, file_path)

    target = os.path.realpath(full_path)
    root = os.path.realpath(working_directory)
    
    if os.path.commonpath([target, root]) != root:
        return f'Error: Cannot write to "{file_path}" as it is outside the permitted working directory'
    
    if not os.path.exists(os.path.dirname(target)):
        try:
            os.makedirs(os.path.dirname(target), exist_ok=True)
        except Exception as e:
            return f'Error creating directory: {e}'
    if os.path.exists(target) and os.path.isdir(target):
        return f'Error: "{file_path}" is a directory, not a file'
    try:
        with open(target, "w") as f:
            f.write(content)
        
        return f'Successfully wrote to "{file_path}" ({len(content)} characters written)'
    
    except Exception as e:
        return f'Error writing to file: {e}'
    
    
schema_write_file = types.FunctionDeclaration(
    name="write_file",
    description="Writes content to a file within the working directory. Creates the file if it doesn't exist.",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="The file path to the file to write, relative to the working directory. If not provided, list files in the working directory itself.",
            ),
            "content": types.Schema(
                type=types.Type.STRING,
                description="The content to write to the file in the file path.",                
            ),
        },
        required=["file_path", "content"],
    ),
)