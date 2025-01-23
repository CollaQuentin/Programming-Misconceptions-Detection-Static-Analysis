import ast
from useless_for_loop_range import Plugin, ERROR_MESSAGE
from typing import Set

TRIVIAL_CASE = """
l = [1, 2, 3, 4, 5]
for x in l:
    print(x)
"""

USELESS_FOR_LOOP_RANGE = """
l = [1, 2, 3, 4, 5]
for i in range(len(l)):
    print(l[i])
"""

USEFUL_FOR_LOOP_RANGE = """
l = [1, 2, 3, 4, 5]
for i in range(len(l)):
    l[i] = 0
"""

def _results(s: str) -> Set[str]:
    tree = ast.parse(s)
    plugin = Plugin(tree)
    return {f'{line}:{col+1} {msg}' for line, col, msg, _ in plugin.run()}

def test_trivial_case():
    assert _results(TRIVIAL_CASE) == set()

def test_useless_for_loop_range():
    assert _results(USELESS_FOR_LOOP_RANGE) == {f"3:1 {ERROR_MESSAGE}"}

def test_useful_for_loop_range():
    assert _results(USEFUL_FOR_LOOP_RANGE) == set()
