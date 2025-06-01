import re

VERSION: str = "1.1"
# PATTERN: re.Pattern = re.compile(r"^([ ]*)if[ ]*(\w+).*:\n+(\1[ ]+.*\n)*\1[ ]+\2[ ]*(\+|-|\*|\/|%|\*\*|\/\/)?=", flags=re.MULTILINE)
PATTERN: re.Pattern = re.compile(r"^([ ]*)if[ ]*([a-zA-Z0-9]+)[^\w].*:\n+((?!else).|\n)*\1[ ]+\2[ ]*(\+|-|\*|\/|%|\*\*|\/\/)?=", flags=re.MULTILINE)

def find_misconception(code: str) -> bool:
    return bool(PATTERN.search(code))
