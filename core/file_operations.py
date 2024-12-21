import os

def create_file(file_name):
    try:
        with open(file_name, 'w') as f:
            pass
        return f"File '{file_name}' created successfully."
    except Exception as e:
        return f"Error creating file '{file_name}': {e}"

def delete_file(file_name):
    try:
        os.remove(file_name)
        return f"File '{file_name}' deleted successfully."
    except FileNotFoundError:
        return f"Error: File '{file_name}' not found."
    except Exception as e:
        return f"Error deleting file '{file_name}': {e}"
