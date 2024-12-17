import re

PRE_CHECK: re.Pattern = re.compile(r"\s*for\s+\w+\s+in")
# PATTERN: re.Pattern = re.compile(r"((\t|[ ]{4})*)for\s+(\w+)\s+in\s+(\w+(\.\w+)?\s*(\((\s*\w+\s*(,\s*\w+\s*)*)?\))?|\[\s*\w+\s*(,\s*\w+\s*)*\s*\]|\(\s*\w+\s*(,\s*\w+\s*)*\s*\)|\{\s*\w+\s*(,\s*\w+\s*)*\s*\})\s*:\n(\1(\t|[ ]{4})+[^\n]*\n)*\1(\t|[ ]{4})+[^\n]*(?<!\w\n)\3(?!\w)[^\n]*")
# PATTERN: re.Pattern = re.compile(r"(^|\s+)for\s+(\w+)\s+in\s+(\w+(\(.*\))?|(?:\[|\(|\{).*(?:\]|\)\}))\s*:(?!(.|\n)*.*(?<!\w)\2(?!\w))")
# PATTERN: re.Pattern = re.compile(r"(^|\s+)for\s+(\w+)\s+in\s+(\w+(\(.*\))?|(?:\[|\(|\{).*(?:\]|\)\}))\s*:(?!(.|\n)*\1[ ]+.*(?<!\w)\2(?!\w))", flags=re.MULTILINE)
PATTERN: re.Pattern = re.compile(r"(^|[ ]+)for\s+(\w+)\s+in\s+(\w+(\(.*\))?|(?:\[|\(|\{).*(?:\]|\)\}))\s*:(?!(.|\n)*\1[ ]+.*(?<!\w)\2(?!\w))", flags=re.MULTILINE)

def find_misconception(code: str) -> bool:
    # return PRE_CHECK.search(code) and not PATTERN.search(code)
    return PATTERN.search(code)
