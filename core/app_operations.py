import subprocess

def open_app(app_name):
    try:
        subprocess.Popen([app_name], shell=True, stderr=subprocess.PIPE)
        return f"Application '{app_name}' opened successfully."
    except FileNotFoundError:
        return f"Error: Application '{app_name}' not found."
    except Exception as e:
        return f"Error opening application '{app_name}': {e}"

def close_app(app_name):
    return f"Simulated close for '{app_name}' (Feature under construction)."
