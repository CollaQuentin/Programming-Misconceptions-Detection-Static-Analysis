import re

VERSION: str = "1.4"
# PATTERN: re.Pattern = re.compile(r"(?:if|while)\s+\w+\s*(?<!=|!)=\s*\w+")
# PATTERN: re.Pattern = re.compile(r"^[ ]*(?:if|while)\s+\w+\s*(?<!=|!)=\s*\w+", flags=re.MULTILINE)
# PATTERN: re.Pattern = re.compile(r"^[ ]*(?:if|while)[ ]+\w+[ ]*(?<!=|!)=[ ]*\w+", flags=re.MULTILINE)
# PATTERN: re.Pattern = re.compile(r"^[ ]*(?:if|elif|while)[ ]+\w+[ ]*(?<!=|!)=[ ]*\w+", flags=re.MULTILINE)
PATTERN: re.Pattern = re.compile(r"^[ ]*(?:if|elif|while)[ ]+(\([ ]*)?\w+[ ]*(?<!=|!)=[ ]*\w+([ ]*\))?", flags=re.MULTILINE)

def find_misconception(code: str) -> bool:
    return bool(PATTERN.search(code))
