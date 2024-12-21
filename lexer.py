import re

class CommandLexer:
    def __init__(self):
        self.token_specification = [
            ('ACTION', r'open|delete|create|close', re.IGNORECASE),
            ('TARGET', r'[a-zA-Z0-9_.]+'),
            ('WHITESPACE', r'\\s+', None),
        ]
        self.token_regex = self._compile_regex()

    def _compile_regex(self):
        parts = [f'(?P<{name}>{pattern})' for name, pattern, _ in self.token_specification]
        return re.compile('|'.join(parts))

    def tokenize(self, command):
        for match in self.token_regex.finditer(command):
            token_type = match.lastgroup
            if token_type != 'WHITESPACE':
                yield token_type, match.group(token_type)
