import ast
from init_should_return import Plugin, ERROR_MESSAGE
from typing import Set

TRIVIAL_CASE = """
class Dog:
    def __init__(self, name):
        self.name = name

    def get_name(self):
        return self.name

    def bark(self):
        print("Woof !")
"""

NO_INIT = """
class Dog:
    def bark(self):
        print("Woof !")
"""

SIMPLE_RETURN = """
class Dog:
    def __init__(self):
        return Dog()

    def bark(self):
        print("Woof !")
"""

RETURN_WITH_ATTRIBUTES = """
class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        return Dog(name, age)

    def get_name(self):
        return self.name

    def get_age(self):
        return self.age

    def bark(self):
        print("Woof !")
"""

RETURN_EXPR = """
class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        return "Dog created"
"""



def _results(s: str) -> Set[str]:
    tree = ast.parse(s)
    plugin = Plugin(tree)
    return {f'{line}:{col+1} {msg}' for line, col, msg, _ in plugin.run()}

def test_trivial_case():
    assert _results(TRIVIAL_CASE) == set()

def test_no_init():
    assert _results(NO_INIT) == set()

def test_simple_return():
    assert _results(SIMPLE_RETURN) == {f"3:5 {ERROR_MESSAGE}"}

def test_return_with_attributes():
    assert _results(RETURN_WITH_ATTRIBUTES) == {f"3:5 {ERROR_MESSAGE}"}

def test_return_expr():
    assert _results(RETURN_EXPR) == {f"3:5 {ERROR_MESSAGE}"}