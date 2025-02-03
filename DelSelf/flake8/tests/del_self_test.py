import ast
from del_self import Plugin, ERROR_MESSAGE
from typing import Set


TRIVIAL_CASE = """
class Dog:
    def __init__(self, name):
        self.name = name

    def bark(self):
        print("Woof !")
"""

DEL_SELF = """
class Bomb:
    def destroy(self):
        del self
"""

def _results(s: str) -> Set[str]:
    tree = ast.parse(s)
    plugin = Plugin(tree)
    return {f'{line}:{col+1} {msg}' for line, col, msg, _ in plugin.run()}

def test_trivial_case():
    assert _results(TRIVIAL_CASE) == set()

def test_del_self():
    assert _results(DEL_SELF) == {f"4:9 {ERROR_MESSAGE}"}

