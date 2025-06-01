import ast
from cannot_chain_member_accesses import Plugin, ERROR_MESSAGE
from typing import Set

TRIVIAL_CASE = """
print(node.next.value)
"""

CANNOT_CHAIN_MEMBER_ACCESSES = """
n = node.next()
print(n.value)
"""

IN_FUNCTION = """
def foo(node):
    n = node.next()
    return n.value
"""

TEST = """
def remove(self):
    nexxt = self.__head
    for i in range(self.__length):
        nexxt = nexxt.next()
"""

def _results(s: str) -> Set[str]:
    tree = ast.parse(s)
    plugin = Plugin(tree)
    return {f'{line}:{col+1} {msg}' for line, col, msg, _ in plugin.run()}

def test_trivial_case():
    assert _results(TRIVIAL_CASE) == set()

def test_cannot_chain_member_accesses():
    assert _results(CANNOT_CHAIN_MEMBER_ACCESSES) == {f"2:1 {ERROR_MESSAGE}"}

def test_in_function():
    assert _results(IN_FUNCTION) == {f"3:5 {ERROR_MESSAGE}"}

def test_test():
    assert _results(TEST) == set()
