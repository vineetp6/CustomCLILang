# import subprocess

# def open_app(app_name):
#     try:
#         subprocess.Popen([app_name], shell=True, stderr=subprocess.PIPE)
#         return f"Application '{app_name}' opened successfully."
#     except FileNotFoundError:
#         return f"Error: Application '{app_name}' not found."
#     except Exception as e:
#         return f"Error opening application '{app_name}': {e}"

# def close_app(app_name):
#     return f"Simulated close for '{app_name}' (Feature under construction)."

import os
import subprocess
from typing import List

def search_and_open_file(keyword: str, search_path: str = ".", recursive: bool = True):
    """
    Search for files containing the keyword in the given directory and open the first match.
    
    Args:
        keyword (str): The keyword to search for in file names.
        search_path (str): The directory to search in.
        recursive (bool): Whether to search subdirectories.
    
    Returns:
        str: A message indicating the result of the operation.
    """
    matches = []

    # Walk through the directory to find matches
    for root, dirs, files in os.walk(search_path):
        for file in files:
            if keyword.lower() in file.lower():
                matches.append(os.path.join(root, file))
        if not recursive:
            break  # Stop if not searching recursively

    if matches:
        file_to_open = matches[0]  # Open the first matching file
        try:
            if os.name == "nt":  # For Windows
                os.startfile(file_to_open)
            elif os.name == "posix":  # For macOS/Linux
                subprocess.call(["open", file_to_open])
            return f"Opened: {file_to_open}"
        except Exception as e:
            return f"Error opening file: {e}"
    else:
        return "No matching files found."
