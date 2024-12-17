import re

PATTERN: re.Pattern = re.compile(r"([ ]*)(for\s+(\w+)\s+in\s+(\w+\s*(\(.*\))?|\[.*\]|\(.*\)|\{.*\})\s*:\s*\n)(?=(\n|.)*\1[ ]+(\3)\s*(\+|-|\/|\/\/|%|\*|\|)?=[^=]\s*)")

def find_misconception(code: str) -> bool:
    return bool(PATTERN.search(code))
