import ast
from variables_have_default_value import Plugin, ERROR_MESSAGE
from typing import Set

TRIVIAL_CASE = """
x = 3
print(x)
x += 1
print(x)
"""

UNDEFINED_VARIABLE = """
print(x)
"""

UNDEFINED_VARIABLE_AUGASSIGN = """
x = x + 1
"""

UNDEFINED_IN_FUNCTION = """
def foo(a, b, c):
    print(d)
"""

DEFINED_ARGUMENT = """
def fact(n):
    if n == 0: return 1
    return n * fact(n-1)
"""

INT_FUNCTION = """
def fact(n):
    if int(n) >= 1:
        for n in range(1,int(n+1)):
            k *= n
            print(k)
"""

def _results(s: str) -> Set[str]:
    tree = ast.parse(s)
    plugin = Plugin(tree)
    return {f'{line}:{col+1} {msg}' for line, col, msg, _ in plugin.run()}

def test_trivial_case():
    assert _results(TRIVIAL_CASE) == set()

def test_undefined_variable():
    assert _results(UNDEFINED_VARIABLE) == {f"2:7 {ERROR_MESSAGE}"}

def test_undefined_varaible_augassign():
    assert _results(UNDEFINED_VARIABLE_AUGASSIGN) == {f"2:5 {ERROR_MESSAGE}"}

def test_undefined_in_function():
    assert _results(UNDEFINED_IN_FUNCTION) == {f"3:11 {ERROR_MESSAGE}"}

def test_defined_argument():
    assert _results(DEFINED_ARGUMENT) == set()

def test_int_function():
    assert _results(INT_FUNCTION) == set()