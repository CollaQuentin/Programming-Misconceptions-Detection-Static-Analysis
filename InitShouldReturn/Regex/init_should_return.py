import re

PATTERN: re.Pattern = re.compile(r"([ ]*)def\s+__init__\s*\(\s*\w+\s*(\s*,\s*\w*\s*)*\):((\n+|.)(?!def ))*\1[ ]+return")
def find_misconception(code: str) -> bool:
    return bool(PATTERN.search(code))

