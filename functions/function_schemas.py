schema_get_files_info = {
    "type": "function",
    "function": {
        "name": "get_files_info",
        "description": "Lists files in a specified directory relative to the working directory, providing file size and directory status",
        "parameters": {
            "type": "object",
            "properties": {
                "directory": {
                    "type": "string",
                    "description": "Directory path to list files from, relative to the working directory (default is the working directory itself)",
                },
            },
            "required":["directory"],
        },
    },
}

schema_get_file_content = {
    "type": "function",
    "function": {
        "name": "get_file_content",
        "description": "Reads the content of a file in the working directory. Long files are truncated at a maximum number of characters, with a note added at the end",
        "parameters": {
            "type": "object",
            "properties": {
                "file_path": {
                    "type": "string",
                    "description": "Path to the file to read, relative to the working directory",
                },
            },
            "required": ["file_path"],
        },
    },
}
schema_run_python_file ={
        "type": "function",
        "function": {
            "name": "run_python_file",
            "description": "Runs a Python file (for example main.py) and returns its output and exit code. Use this when the user asks to run or execute a file",
            "parameters": {
                "type": "object",
                "properties": {
                    "file_path": {
                        "type": "string",
                        "description": "Path to the Python file to run, relative to the working directory",
                    },
                    "args": {
                        "type": "array",
                        "items": {"type": "string"},
                        "description": "Optional list of command-line arguments to pass to the Python file",
                    },
                },
                "required": ["file_path"],
            },
        },
    }

schema_write_file ={
    "type": "function",
    "function": {
        "name": "write_file",
        "description": "Writes content to a file in the working directory, creating the file and any missing folders. Overwrites the file if it already exists",
        "parameters": {
            "type": "object",
            "properties": {
                "file_path": {
                    "type": "string",
                    "description": "Path to the file to write, relative to the working directory",
                },
                "content": {
                    "type": "string",
                    "description": "The text content to write into the file",
                },
            },
            "required": ["file_path", "content"],
            },
        },
    }



available_functions = [
    schema_get_files_info, schema_get_file_content,schema_write_file,schema_run_python_file,
]