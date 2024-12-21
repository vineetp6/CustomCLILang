from lexer import CommandLexer
from parser import CommandParser

def main():
    print("Custom CLI Language Interpreter (Type 'exit' to quit)")
    lexer = CommandLexer()
    parser = CommandParser()

    while True:
        try:
            command = input(">>> ").strip()
            if command.lower() == "exit":
                print("Exiting the interpreter. Goodbye!")
                break

            tokens = lexer.tokenize(command)
            result = parser.parse_and_execute(tokens)
            print(result)
        except Exception as e:
            print(f"Error: {e}")

if __name__ == "__main__":
    main()
