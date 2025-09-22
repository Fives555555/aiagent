import os

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