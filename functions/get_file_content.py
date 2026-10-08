import os
from config import MAX_CHARS

def get_file_content(working_directory: str, file_path: str) -> str:
    try:
        working_directory_full_path = os.path.abspath(working_directory)
        new_file_path = os.path.normpath(os.path.join(working_directory_full_path, file_path))
        if os.path.commonpath([working_directory_full_path,new_file_path]) != working_directory_full_path:
            return f'Error: Cannot read "{new_file_path}" as it is outside the permitted working directory'
        if not os.path.isfile(new_file_path):
            return f'Error: File not found or is not a regular file: "{file_path}"'

        

        with open(new_file_path, "r") as f:
            file_content_string = f.read(MAX_CHARS)
            
            # After reading the first MAX_CHARS...
            if f.read(1):
                file_content_string += f'[...File "{new_file_path}" truncated at {MAX_CHARS} characters]'
                
            return file_content_string
    except Exception as e:
        return( f"Error:{e}")