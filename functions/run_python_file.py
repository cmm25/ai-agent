import os 

def run_python_file(
    working_directory: str, file_path: str, args: list[str] | None = None
) -> str:
    try:
        full_working_path = os.path.normpath(os.path.abspath(working_directory))
        full_file_path = full_file_path = os.path.normpath(os.path.join(full_working_path, file_path))

        if os.path.commonpath([full_working_path, full_file_path]) != full_working_path:
            return f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory'
        if not os.path.isfile(full_file_path):
            return f'Error: "{file_path}" does not exist or is not a regular file'
        
        if not full_file_path.endswith(".py"):
            return f'Error: "{file_path}" is not a Python file'
        
        # Building program subprocess

        import subprocess 

        command = ["python", full_file_path]
        if args:
            command.extend(args)
        run_result = subprocess.run(command, capture_output= True, text = True, timeout=30)
        return_code_run_result = run_result.returncode
        run_result_output = run_result.stdout
        run_result_error = run_result.stderr

        output_string=""
        if not  return_code_run_result == 0:
            output_string+= f"Process exited with code {return_code_run_result}"
        if not run_result_output and not run_result_error:
            output_string+= f"No output produced"
        else:
            output_string+= f"STDOUT:{run_result_output}"
            output_string += f"STDERR:{run_result_error}"
        return output_string
        
    except Exception as e:
        return f"Error: {e}"