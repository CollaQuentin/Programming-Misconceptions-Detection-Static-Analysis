import ast
from new_attributes_in_method import Plugin, ERROR_MESSAGE
from typing import Set

TRIVIAL_CASE = """
class Dog:
    def __init__(self, name):
        self.name = name
        self.puppy = None

    def set_name(self, name):
        self.name = name
    
    def get_name(self, name):
        return self.name

    def give_birth(self, puppy_name):
        self.puppy = Dog(puppy_name)
"""

NEW_ATTRIBUTE_IN_METHOD = """
class Dog:
    def __init__(self, name):
        self.name = name

    def set_name(self, name):
        self.name = name
    
    def get_name(self, name):
        return self.name

    def give_birth(self, puppy_name):
        self.puppy = Dog(puppy_name)
"""


def _results(s: str) -> Set[str]:
    tree = ast.parse(s)
    plugin = Plugin(tree)
    return {f'{line}:{col+1} {msg}' for line, col, msg, _ in plugin.run()}

def test_trivial_case():
    assert _results(TRIVIAL_CASE) == set()

def test_new_attribute_in_method():
    assert _results(NEW_ATTRIBUTE_IN_METHOD) == {f"13:9 {ERROR_MESSAGE}"}
