# from lexer import CommandLexer
# from parser import CommandParser

# def main():
#     print("Custom CLI Language Interpreter (Type 'exit' to quit)")
#     lexer = CommandLexer()
#     parser = CommandParser()

#     while True:
#         try:
#             command = input(">>> ").strip()
#             if command.lower() == "exit":
#                 print("Exiting the interpreter. Goodbye!")
#                 break

#             tokens = lexer.tokenize(command)
#             result = parser.parse_and_execute(tokens)
#             print(result)
#         except Exception as e:
#             print(f"Error: {e}")

# if __name__ == "__main__":
#     main()

from core.app_operations import search_and_open_file

def interpret_command(command: str):
    """
    Interpret and execute user commands.
    
    Args:
        command (str): The user command as a string.
    
    Returns:
        str: A message indicating the result of the operation.
    """
    command_parts = command.strip().split(maxsplit=1)

    if len(command_parts) < 2:
        return "Invalid command. Usage: open <keyword>"

    action, args = command_parts

    if action.lower() == "open":
        # Pass the keyword to the search_and_open_file function
        return search_and_open_file(args)
    else:
        return f"Unknown command: {action}"
