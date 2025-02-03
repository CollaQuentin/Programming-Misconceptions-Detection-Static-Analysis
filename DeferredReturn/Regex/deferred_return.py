import re

VERSION: str = "1.0"
PATTERN: re.Pattern = re.compile(r"^([ ]*)return.*\n\1\w", flags=re.MULTILINE)

def find_misconception(code: str) -> bool:
    return bool(PATTERN.search(code))
