import ast
from objects_must_be_named import Plugin, ERROR_MESSAGE
from typing import Set

# In the following examples, we suppose the following Dog class : 
# class Dog:
#     def __init__(self, name):
#         self.name = name
# 
#     def bark(self):
#         print("Wouf !")


HEY = """
import math 
n=10
for i in range(1,n+1):
    print(math.sin(math.pi/i))
"""

TRIVIAL_CASE = """
d = Dog("Steve")
d.bark()
print(f"My dog is named {d.name} :)")
"""

USELESS_INSTANCE = """
d = Dog("Steve")
d.bark()
"""

ONE_LINER = """
Dog("Steve").bark()
"""

USELESS_INT_STORAGE = """
a = 1
print(a)
"""

USEFUL_INT_STORAGE = """
a = 1
a += 3
print(a)
"""

MULTIPLE_ASSIGNMENTS = """
a = b = c = 7
a += 1
print(a)
"""

TUPLE_ASSIGNMENTS = """
(a,b) = (1,2)
a += 1
print(a)
"""

USED_IN_LOOP = """
a = 1
for i in range(10):
    print(a)
"""

ASSIGNED_IN_LOOP = """
for i in range(10):
    a = 1
    print(a)
"""

def _results(s: str) -> Set[str]:
    tree = ast.parse(s)
    plugin = Plugin(tree)
    return {f'{line}:{col+1} {msg}' for line, col, msg, _ in plugin.run()}

def test_hey():
    assert _results(HEY) == {f"2:1 {ERROR_MESSAGE.format('n')}"}

def test_trivial_case():
    assert _results(TRIVIAL_CASE) == set()

def test_useless_instance():
    assert _results(USELESS_INSTANCE) == {f"2:1 {ERROR_MESSAGE.format('d')}"}

def test_one_liner():
    assert _results(ONE_LINER) == set()

def test_useless_int_storage():
    assert _results(USELESS_INT_STORAGE) == {f"2:1 {ERROR_MESSAGE.format('a')}"}

def test_useful_int_storage():
    assert _results(USEFUL_INT_STORAGE) == set()

def test_multiple_assignments():
    assert _results(MULTIPLE_ASSIGNMENTS) == {
        f"2:5 {ERROR_MESSAGE.format('b')}",
        f"2:9 {ERROR_MESSAGE.format('c')}"
    }

def test_tuple_assignments():
    assert _results(TUPLE_ASSIGNMENTS) == {f"2:4 {ERROR_MESSAGE.format('b')}"}

def test_used_in_loop():
    assert _results(USED_IN_LOOP) == set()

def test_assign_in_loop():
    assert _results(ASSIGNED_IN_LOOP) == {f"3:5 {ERROR_MESSAGE.format('a')}"}