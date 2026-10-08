import os

def write_file(working_directory: str, file_path: str, content: str) -> str:
    try:
        full_path_working = os.path.abspath(working_directory)
        full_file_path = os.path.normpath(os.path.join(full_path_working, file_path))

        if not os.path.commonpath([full_path_working, full_file_path]) == full_path_working:
            return f'Error: Cannot write to "{file_path}" as it is outside the permitted working directory'
        if os.path.isdir(full_file_path):
            return f'Error: Cannot write to "{file_path}" as it is a directory'

        "here what we are doing is checking the dir section of the file path"
        "note that full_file_path is just a string so we have to recreate folders"
        "to make it functional"
        os.makedirs(os.path.dirname(full_file_path), exist_ok= True)

        with open(full_file_path, "w") as f:
            if f.write(content):
                return f'Successfully wrote to "{full_file_path}" ({len(content)} characters written)'
    except Exception as e:
        return f"Error: {e}"