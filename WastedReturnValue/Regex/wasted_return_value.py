import re

VERSION: str = "1.0"
PATTERN: re.Pattern = re.compile(r"^([ ]*)def[ ]+(\w+)\([^\n]*\):((\n+|.)(?!def ))*\1[ ]+return[ ]+[^\n]+(?=(.|\n)*^[ ]*\2\([^\n]*\))", flags=re.MULTILINE)

def find_misconception(code: str) -> bool:
    return bool(PATTERN.search(code))
