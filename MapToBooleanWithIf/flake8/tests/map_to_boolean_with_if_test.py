import ast
from map_to_boolean_with_if import Plugin, ERROR_MESSAGE
from typing import Set

TRIVIAL_CASE = """
a = 3
bigger_than_five = a > 5
"""

TRIVIAL_CASE_FUNCTION = """
def foo(bar):
    return bar > 5
"""

MAP_TO_BOOLEAN_IF = """
a = 3
if a > 5:
    bigger_than_five = True
else:
    bigger_than_five = False
"""

MAP_TO_BOOLEAN_RETURN = """
def foo(bar):
    if bar > 5:
        return True
    else:
        return False
"""

def _results(s: str) -> Set[str]:
    tree = ast.parse(s)
    plugin = Plugin(tree)
    return {f'{line}:{col+1} {msg}' for line, col, msg, _ in plugin.run()}

def test_trivial_case():
    assert _results(TRIVIAL_CASE) == set()

def test_trivial_case_function():
    assert _results(TRIVIAL_CASE_FUNCTION) == set()

def test_map_to_boolean_if():
    assert _results(MAP_TO_BOOLEAN_IF) == {f"3:1 {ERROR_MESSAGE}"}

def test_map_to_boolean_return():
    assert _results(MAP_TO_BOOLEAN_RETURN) == {f"3:5 {ERROR_MESSAGE}"}