import ast
from init_creates import Plugin, ERROR_MESSAGE
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

CREATES_OBJECT = """
class Dog:
    def __init__(self, name):
        self.name = name
        dog = Dog(name)

    def bark(self):
        print("Woof !")
"""

CREATES_OBJECT_NESTED = """
class Dog:
    def __init__(self, name):
        self.name = name
        if name.endswith("new"):
            if len(name) == 3:
                dog = Dog(name)
"""

CREATES_OTHER_OBJECT = """
class Dog:
    def __init__(self, name):
        self.name = name

class Human:
    def __init__(self, name, pet_name):
        self.name = name
        self.pet = Dog(pet_name)
"""

def _results(s: str) -> Set[str]:
    tree = ast.parse(s)
    plugin = Plugin(tree)
    return {f'{line}:{col+1} {msg}' for line, col, msg, _ in plugin.run()}

def test_trivial_case():
    assert _results(TRIVIAL_CASE) == set()

def test_no_init():
    assert _results(NO_INIT) == set()

def test_creates_object():
    assert _results(CREATES_OBJECT) == {f"3:5 {ERROR_MESSAGE}"}

def test_creates_object_nested():
    assert _results(CREATES_OBJECT_NESTED) == {f"3:5 {ERROR_MESSAGE}"}

def test_creates_other_object():
    assert _results(CREATES_OTHER_OBJECT) == set()
