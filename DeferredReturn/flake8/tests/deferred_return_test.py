import ast
from deferred_return import Plugin, ERROR_MESSAGE
from typing import Set

TRIVIAL_CASE = """
def foo(bar):
    print("This is before the return")
    if bar > 5:
        print("This is in the condition")
        return bar
    print("This is after the condition")
    return bar
"""

DEFERRED_RETURN = """
def foo(bar):
    if bar > 5:
        return bar
        print("This will never print")
    return bar
"""

SHORT_FUNCTION = """
def foo(bar):
    return bar
    print(bar)
"""

def _results(s: str) -> Set[str]:
    tree = ast.parse(s)
    plugin = Plugin(tree)
    return {f'{line}:{col+1} {msg}' for line, col, msg, _ in plugin.run()}

def test_trivial_case():
    assert _results(TRIVIAL_CASE) == set()

def test_deferred_retrun():
    assert _results(DEFERRED_RETURN) == {f"5:9 {ERROR_MESSAGE}"}

def test_short_function():
    assert _results(SHORT_FUNCTION) == {f"4:5 {ERROR_MESSAGE}"}