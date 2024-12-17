import re

PRE_CHECK: re.Pattern = re.compile(r"\w+\s+=\s+.*")
# PATTERN: re.Pattern = re.compile(r"(^|\s+)(([\w]+)\s*=.*\n+)(?!(.*\n)*.*(?<!\w)(\3)(?!\w).*(.*\n)*.*(?<!\w)(\3)(?!\w).*)")
PATTERN: re.Pattern = re.compile(r"(^|\s+)(([\w]+)\s*=([^=\n]*)\n+)(?!(.*\n)*.*(?<!\w)\3(?!\w).*(.*\n)*.*(?<!\w)\3(?!\w).*)", flags=re.MULTILINE)


def find_misconception(code: str) -> bool:
    # return PRE_CHECK.search(code) and not PATTERN.search(code)
    return PATTERN.search(code)
