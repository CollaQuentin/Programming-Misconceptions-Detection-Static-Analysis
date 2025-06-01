import ast
from no_self_parameter import Plugin, ERROR_MESSAGE
from typing import Set

TRIVIAL_CASE = """
class Dog:
    def __init__(self, name):
        self.name = name

    def get_name(self):
        return self.name

    def bark(self):
        print("Bark !")
"""

MISSING_SELF_IN_INIT = """
class Dog:
    def __init__(name):
        self.name = name

    def get_name(self):
        return self.name

    def bark(self):
        print("Bark !")
"""

MISSING_SELF_IN_OTHER_METHOD = """
class Dog:
    def __init__(self, name):
        self.name = name
    
    def get_name(self):
        return self.name

    def bark():
        print("Bark !")
"""

NESTED_CLASSES = """
class A:
    class B:
        def __init__(self, value):
            self.value = value

    def __init__():
        pass
"""

def _results(s: str) -> Set[str]:
    tree = ast.parse(s)
    plugin = Plugin(tree)
    return {f'{line}:{col+1} {msg}' for line, col, msg, _ in plugin.run()}

def test_trivial_case():
    assert _results(TRIVIAL_CASE) == set()

def test_missing_self_in_init():
    assert _results(MISSING_SELF_IN_INIT) == {f"3:5 {ERROR_MESSAGE}"}

def test_missing_self_in_other_method():
    assert _results(MISSING_SELF_IN_OTHER_METHOD) == {f"9:5 {ERROR_MESSAGE}"}

def test_nested_class():
    assert _results(NESTED_CLASSES) == {f"7:5 {ERROR_MESSAGE}"}
