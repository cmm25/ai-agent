import os 

def get_files_info(working_directory:str, directory:str =".")->str:
    try:

        absolute_path = os.path.abspath(working_directory)
        target_path = os.path.normpath(os.path.join(absolute_path, directory))
        if not os.path.commonpath([absolute_path, target_path])== absolute_path:
            return (f'Error: Cannot list "{directory}" as it is outside the permitted working directory')

        if not os.path.isdir(target_path):
                    return (f'Error: "{directory}" is not a directory')

        #list files part

        lines = []
        for item in os.listdir(target_path):
            item_path = os.path.join(target_path, item)        
            size=os.path.getsize(item_path)
            dir_validity=os.path.isdir(item_path)
            lines.append(f"- {item}: file_size={size} bytes, is_dir={dir_validity}")
        return "\n".join(lines)
    except Exception as e :
        return f"Error: {e}"

