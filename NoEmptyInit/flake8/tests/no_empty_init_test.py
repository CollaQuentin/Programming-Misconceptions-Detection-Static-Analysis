import ast
from no_empty_init import Plugin, ERROR_MESSAGE
from typing import Set

TRIVIAL_CASE = """
class Test:
    def __init__(self):
        self.a = 1
        self.b = 2

    def get_a(self):
        return self.a

    def get_b(self):
        return self.b
"""

NO_INIT = """
class Dog:
    def bark(self):
        print("Woof !")
"""

PASS_INIT = """
class Dog:
    def __init__(self):
        pass
        
    def bark(self):
        print("Woof !")
"""

RETURN_INIT = """
class Dog:
    def __init__(self):
        return None
    
    def bark(self):
        print("Woof !")
"""

DOCSTRING = """
class Dog:
    def __init__(self):
        \"\"\"
        This is the docstring of the class
        \"\"\"
"""

ELLIPSIS = """
class Dog:
    def __init__(self):
        ...
"""
def _results(s: str) -> Set[str]:
    tree = ast.parse(s)
    plugin = Plugin(tree)
    return {f'{line}:{col+1} {msg}' for line, col, msg, _ in plugin.run()}

def test_trivial_case():
    assert _results(TRIVIAL_CASE) == set()

def test_no_init():
    assert _results(NO_INIT) == set()

def test_pass_init():
    assert _results(PASS_INIT) == {f"3:5 {ERROR_MESSAGE}"}

def test_return_init():
    assert _results(RETURN_INIT) == {f"3:5 {ERROR_MESSAGE}"}

def test_docstring():
    assert _results(DOCSTRING) == {f"3:5 {ERROR_MESSAGE}"}

def test_ellipsis():
    assert _results(ELLIPSIS) == {f"3:5 {ERROR_MESSAGE}"}
