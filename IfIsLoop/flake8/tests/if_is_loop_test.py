import ast
from if_is_loop import Plugin, ERROR_MESSAGE
from typing import Set

TRIVIAL_CASE = """
if x < 10:
    print("x is smaller than 10")
    min = x
"""

IF_IS_LOOP = """
if x < 10:
    x += 1
    print(x)
"""

def _results(s: str) -> Set[str]:
    tree = ast.parse(s)
    plugin = Plugin(tree)
    return {f'{line}:{col+1} {msg}' for line, col, msg, _ in plugin.run()}

def test_trivial_case():
    assert _results(TRIVIAL_CASE) == set()

def test_if_is_loop():
    assert _results(IF_IS_LOOP) == {f"2:1 {ERROR_MESSAGE}"}
