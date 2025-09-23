import os
import sys
import subprocess

def run_python_file(working_directory, file_path, args=None):
    full_path = os.path.join(working_directory, file_path)
    target = os.path.realpath(full_path)
    root = os.path.realpath(working_directory)
    
    if os.path.commonpath([target, root]) != root:
        return f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory'
    if not os.path.exists(target):
        return f'Error: File "{file_path}" not found.'
    if not file_path.endswith(".py"):
        return f'Error: "{file_path}" is not a Python file.'

    try:
        cmd = ["python", target]
        if args:
            cmd.extend(args)    
        completed_process = subprocess.run(cmd, cwd=root, capture_output=True, timeout=30, text=True, check=False)
        output = []
        if completed_process.stdout:
            output.append(f"STDOUT:\n{completed_process.stdout}")
        if completed_process.stderr:
            output.append(f"STDERR:\n{completed_process.stderr}")

        if completed_process.returncode != 0:
            output.append(f"Process exited with code {completed_process.returncode}")
            
        return "\n".join(output) if output else "No output produced."

    except Exception as e:
        return f"Error: executing Python file: {e}"

