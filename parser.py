from core.file_operations import create_file, delete_file
from core.app_operations import open_app, close_app

class CommandParser:
    def __init__(self):
        self.actions = {
            'open': open_app,
            'delete': delete_file,
            'create': create_file,
            'close': close_app,
        }

    def parse_and_execute(self, tokens):
        tokens = list(tokens)
        if len(tokens) < 2:
            return "Error: Command must have an action and a target."

        action, target = tokens[0][1].lower(), tokens[1][1]
        if action in self.actions:
            try:
                return self.actions[action](target)
            except Exception as e:
                return f"Error executing action '{action}' on target '{target}': {e}"
        else:
            return f"Error: Unknown action '{action}'."
