import re

VERSION: str = "1.2"
# PATTERN: re.Pattern = re.compile(r"self[ ]*=", flags=re.MULTILINE)
# PATTERN: re.Pattern = re.compile(r"self[ ]*=[ ]*", flags=re.MULTILINE)
PATTERN: re.Pattern = re.compile(r"^[ ]*self[ ]*=[ ]*", flags=re.MULTILINE)

def find_misconception(code: str) -> bool:
    return bool(PATTERN.search(code))
