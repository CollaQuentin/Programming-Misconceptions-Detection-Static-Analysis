import re

VERSION: str = "1.1"
# PATTERN: re.Pattern = re.compile(r"^([ ]*)(for[ ]+(\w+)[ ]+in[ ]+range[ ]*\([ ]*len[ ]*\([^\n]+\)[ ]*\)[ ]*:\n+)(?!(\1[ ]+[^\n]+\n+)*\1[ ]+[^\n]*\[\3\][ ]*=)", flags=re.MULTILINE)
PATTERN: re.Pattern = re.compile(r"^([ ]*)(for[ ]+(\w+)[ ]+in[ ]+range[ ]*\([ ]*len[ ]*\([^\n]+\)[ ]*\)[ ]*:\n+)(?!(.|\n)*^\1[ ]+[^\n]+\[\3\][ ]*=)", flags=re.MULTILINE)

def find_misconception(code: str) -> bool:
    return bool(PATTERN.search(code))
