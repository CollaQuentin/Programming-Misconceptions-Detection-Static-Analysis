import ast
from wasted_return_value import Plugin, ERROR_MESSAGE
from typing import Set

TRIVIAL_CASE = """
def foo(bar):
    return -bar

print(foo(5))
"""

STORED_RETURN = """
def foo(bar):
    return -bar

opposite = foo(5)
"""

RETURN_NONE = """
def foo(bar):
    return None

foo(5)
"""

RETURN = """
def foo(bar):
    return

foo(5)
"""

WASTED_RETURN_VALUE = """
def foo(bar):
    return -bar

foo(5)
"""

TEST = """
def rho(a,b,c):
    return b**2 - 4*a*c

def n_solutions(a,b,c):
    if rho(a,b,c) > 0 :
        return 2
    elif rho(a,b,c) == 0 :
        return 1
    else :
        return 0
def solution(a,b,c):
    if n_solutions(a,b,c) > 1 :
        if a > 0:
            return (-b - math.sqrt(rho(a, b, c)))/(2*a)
        else:
            return (-b + math.sqrt(rho(a, b, c)))/(2*a)
    elif n_solutions(a, b, c) == 1:
        return (-b+rho(a, b, c))/(2*a)
    else:
        return None
"""

TEST2 = """
def rho(a,b,c):
    return (b**2)-(4*a*c)

def n_solutions(a,b,c):
    if rho(a,b,c) == 0:
        return 1
    elif rho(a,b,c) > 0:
        return 2
    else:
        return 0

def solution(a,b,c):
    if rho(a,b,c) == 0:
        return -b/(2*a)

    elif rho(a,b,c):
        x = (-b+racine_carree(rho(a,b,c)))/2*a
        y = (-b-racine_carree(rho(a,b,c)))/2*a
        if x<y:
            return x
        else:
            return y
"""

def _results(s: str) -> Set[str]:
    tree = ast.parse(s)
    plugin = Plugin(tree)
    return {f'{line}:{col+1} {msg}' for line, col, msg, _ in plugin.run()}

def test_trivial_case():
    assert _results(TRIVIAL_CASE) == set()

def test_stored_return():
    assert _results(STORED_RETURN) == set()

def test_return_none():
    assert _results(RETURN_NONE) == set()

def test_return():
    assert _results(RETURN) == set()

def test_wasted_return_value():
    assert _results(WASTED_RETURN_VALUE) == {f"5:1 {ERROR_MESSAGE}"}

def test_TEST():
    assert _results(TEST) == set()

def test_TEST2():
    assert _results(TEST2) == set()