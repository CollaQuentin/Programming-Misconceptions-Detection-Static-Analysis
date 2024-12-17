import re

PATTERN: re.Pattern = re.compile(r"((\t|[ ]{4})*)def\s+__init__\s*\(\s*\w+\s*(,\s*\w+\s*)*\):(\n+\1(\t|[ ]{4})(\"\"\"(.|\n)*\"\"\"))?(\n+\1((\t|[ ]{4})(return(\s+None)?|pass|\.\.\.)|[^\s]))")


def find_misconception(code: str) -> bool:
    return bool(PATTERN.search(code))
