import re

# PATTERN: re.Pattern = re.compile(r"\s*class\s+(\w+)\s*:\s*\n+(.|\n)*(\s*)def\s+__init__\s*\(\s*\w+\s*(,\s*\w+\s*)*\)\s*:(\n+|.(?!def ))*\2[ ]+.*\1\(")
PATTERN: re.Pattern = re.compile(r"\s*class\s+(\w+)\s*:\s*\n+((\n|.)(?!class\s))*(\s*)def\s+__init__\s*\(\s*\w+\s*(,\s*\w+\s*)*\)\s*:(\n+|.(?!def ))*\2[ ]+.*\1\(")

def find_misconception(code: str) -> bool:
    return bool(PATTERN.search(code))
