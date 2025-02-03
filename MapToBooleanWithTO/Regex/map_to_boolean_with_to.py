import re

VERSION: str = "1.0"
PATTERN: re.Pattern = re.compile(r"(True|False)[ ]+if[^\n]+else[ ]+(True|False)", flags=re.MULTILINE)

def find_misconception(code: str) -> bool:
    return bool(PATTERN.search(code))
