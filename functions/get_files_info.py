import os

def get_files_info(working_directory, directory="."):
    full_path = os.path.join(working_directory, directory)
    try:
        target = os.path.realpath(full_path)
        root = os.path.realpath(working_directory)
        
        if os.path.commonpath([target, root]) != root:
            return f'Error: Cannot list "{directory}" as it is outside the permitted working directory'
        if not os.path.isdir(target):
            return f'Error: "{directory}" is not a directory'
        
        lines = []
        for name in sorted(os.listdir(target)):
            entry_path = os.path.join(target, name)
            size = os.path.getsize(entry_path)
            is_dir = os.path.isdir(entry_path)
            lines.append(f"- {name}: file_size={size} bytes, is_dir={is_dir}")
        return "\n".join(lines)
    except Exception as e:
        return f'Error: {e}'