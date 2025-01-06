import re

PYTHON_RESERVED_KEYWORDS = r"(False|None|True|and|as|assert|async|await|break|class|continue|def|del|elif|else|except|finally|for|from|global|if|import|in|is|lambda|nonlocal|not|or|pass|raise|return|try|while|with|yield)"
VERSION = "1.0"
PATTERN: re.Pattern = re.compile(rf"^[ ]*((def|class)\s+{PYTHON_RESERVED_KEYWORDS}|{PYTHON_RESERVED_KEYWORDS}\s*=)", flags=re.MULTILINE)

def find_misconception(code: str) -> bool:
    return bool(PATTERN.search(code))