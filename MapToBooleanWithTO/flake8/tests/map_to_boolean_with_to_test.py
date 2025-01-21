import ast
from map_to_boolean_with_to import Plugin, ERROR_MESSAGE
from typing import Set

TRIVIAL_CASE = """
x = 5
is_greater_than_10 = x > 10
"""

MAP_TO_BOOLEAN_WITH_TO = """
x = 5
is_greater_than_10 = True if x > 10 else False
"""

MAP_TO_BOOLEAN_WITH_TO_RETURN = """
def is_greater_than_5(x):
    return True if x > 5 else False
"""

def _results(s: str) -> Set[str]:
    tree = ast.parse(s)
    plugin = Plugin(tree)
    return {f'{line}:{col+1} {msg}' for line, col, msg, _ in plugin.run()}

def test_trivial_case():
    assert _results(TRIVIAL_CASE) == set()

def test_map_to_boolean_with_to():
    assert _results(MAP_TO_BOOLEAN_WITH_TO) == {f"3:22 {ERROR_MESSAGE}"}

def test_map_to_boolean_with_to_return():
    assert _results(MAP_TO_BOOLEAN_WITH_TO_RETURN) == {f"3:12 {ERROR_MESSAGE}"}
