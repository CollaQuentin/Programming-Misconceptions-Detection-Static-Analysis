import re

VERSION: str = "1.1"
# PATTERN: re.Pattern = re.compile(r"(^|\s+)(([\w]+)\s*=.*\n+)(?!(.*\n)*.*(?<!\w)(\3)(?!\w).*(.*\n)*.*(?<!\w)(\3)(?!\w).*)")
PATTERN: re.Pattern = re.compile(r"(^|\s+)(([\w]+)\s*=([^=\n]*)\n+)(?!(.*\n)*.*(?<!\w)\3(?!\w).*(.*\n)*.*(?<!\w)\3(?!\w).*)", flags=re.MULTILINE)


def find_misconception(code: str) -> bool:
    return PATTERN.search(code)
