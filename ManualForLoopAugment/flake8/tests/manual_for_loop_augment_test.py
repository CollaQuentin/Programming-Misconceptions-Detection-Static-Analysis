import ast
from manual_for_loop_augment import Plugin, ERROR_MESSAGE
from typing import Set

TRIVIAL_CASE = """
for i in range(10):
    print(i)
"""

REASSIGNED_VARIABLE = """
for i in range(10):
    i = 0
    print(i)
"""

AUGMENTED_VARIABLE = """
for i in range(10):
    i += 1
    print(i)
"""

ASSIGN_TO_PLUS_1 = """
for i in range(10):
    i = i + 1
    print(i)
"""

AUGMENTED_AT_THE_END = """
for i in range(10):
    print(i)
    i += 1
"""

AUGMENTED_IN_IF = """
for i in range(10):
    if i < 5:
        i += 1
    b = 3 * i
    print(b)
"""

REDEFINED_OUTSIDE = """
for i in range(10):
    print(i)
i = 10
"""

def _results(s: str) -> Set[str]:
    tree = ast.parse(s)
    plugin = Plugin(tree)
    return {f'{line}:{col+1} {msg}' for line, col, msg, _ in plugin.run()}

def test_trivial_case():
    assert _results(TRIVIAL_CASE) == set()

def test_reassigned_variable():
    assert _results(REASSIGNED_VARIABLE) == {f"3:5 {ERROR_MESSAGE}"}

def test_augmented_variable():
    assert _results(AUGMENTED_VARIABLE) == {f"3:5 {ERROR_MESSAGE}"}

def test_assign_to_plus_1():
    assert _results(ASSIGN_TO_PLUS_1) == {f"3:5 {ERROR_MESSAGE}"}

def test_augmented_at_the_end():
    assert _results(AUGMENTED_AT_THE_END) == {f"4:5 {ERROR_MESSAGE}"}

def test_augmented_in_if():
    assert _results(AUGMENTED_IN_IF) == {f"4:9 {ERROR_MESSAGE}"}

def test_redefined_outside():
    assert _results(REDEFINED_OUTSIDE) == set()