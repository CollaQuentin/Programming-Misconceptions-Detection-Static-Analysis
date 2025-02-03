import re

VERSION: str = "1.0"
PATTERN: re.Pattern = re.compile(r"^([ ]*)if[ ]+[^\n:]+:\n+\1[ ]+(return[ ]+(True|False)|[\w_]+[ ]*=[ ]*(True|False))[^\n]*\n+\1else:\n+\1[ ]+(return[ ]+(True|False)|[\w_]+[ ]*=[ ]*(True|False))", flags=re.MULTILINE)

def find_misconception(code: str) -> bool:
    return bool(PATTERN.search(code))
