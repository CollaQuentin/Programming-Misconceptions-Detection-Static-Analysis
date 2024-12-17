import re

PATTERN: re.Pattern = re.compile(r"((True|False)\s*(=|!)=|(=|!)=\s*(True|False))")


def find_misconception(code: str) -> bool:
    return bool(PATTERN.search(code))
