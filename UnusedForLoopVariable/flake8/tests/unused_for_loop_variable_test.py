import ast
from unused_for_loop_variable import Plugin, ERROR_MESSAGE
from unused_for_loop_variable import get_names_from_List
from typing import Set

TRIVIAL_CASE = """
for i in range(10):
    print(i)
"""

UNUSED_VARIABLE = """
for i in range(10):
    print('Hello, World !')
"""

TUPLE_UNUSED_VARIABLES = """
l = [('a', 1), ('b', 2), ('c', 3)]
for letter, number in l:
    print(letter)
"""

TUPLE_USED_VARIABLES = """
l = [('a', 1), ('b', 2), ('c', 3)]
for letter, number in l:
    print(letter, number)
"""

LIST_UNUSED_VARIABLES = """
l = [('a', 1), ('b', 2), ('c', 3)]
for [letter, number] in l:
    print(letter)
"""

LIST_USED_VARIABLES = """
l = [('a', 1), ('b', 2), ('c', 3)]
for [letter, number] in l:
    print(letter, number)
"""

USED_AFTER_LOOP = """
for i in range(10):
    print('Hello, World !')
print(i)
"""

LONG_FOR_LOOP = """
for i in range(10):
    print('This is the start of the loop')
    for j in range(10):
        print(j)
    a = 3
    b = a + 1
    function_call(a, b)
    if a < b:
        print(i)
"""

REDEFINED_UNUSED_VARIABLE = """
for i in range(10):
    print('Hello, World !')
i = 25
print(i)
"""

REDEFINED_UNUSED_VARIABLE_IN_LOOP = """
for i in range(10):
    i = 0
    print(i)
"""

REDEFINED_USED_VARIABLE = """
for i in range(10):
    print(i)
i = 25
print(i)
"""

REDEFINED_UNUSED_IN_COMPLICATED_STRUCTURE = """
for i in range(10):
    print('Hello, World !') 
[a, (b,c)] = [d, (e, i)] = [1, (2,3)]
print(i)
"""

UNDERSCORE_VARIABLE = """
for _ in range(10):
    print('This is intentional')
"""

NESTED_FOR_LOOPS = """
for i in range(10):
    for i in range(10):
        print(i)
"""

def _results(s: str) -> Set[str]:
    tree = ast.parse(s)
    plugin = Plugin(tree)
    return {f'{line}:{col+1} {msg}' for line, col, msg, _ in plugin.run()}

def test_get_names_from_List():
    node = ast.parse("[a,(b,c)] = [d,(e,f)] = 1,(2,3)")
    names = []
    for l in node.body[0].targets:
        names.extend(get_names_from_List(l))
    print(sorted(names))
    assert sorted(names) == ['a', 'b', 'c', 'd', 'e', 'f']

def test_trivial_case():
    assert _results(TRIVIAL_CASE) == set()

def test_unused_variable():
    assert _results(UNUSED_VARIABLE) == {f"2:1 {ERROR_MESSAGE}"}

def test_tuple_unused_variables():
    assert _results(TUPLE_UNUSED_VARIABLES) == {f"3:1 {ERROR_MESSAGE}"}

def test_tuple_used_variables():
    assert _results(TUPLE_USED_VARIABLES) == set()

def test_list_unused_variables():
    assert _results(LIST_UNUSED_VARIABLES) == {f"3:1 {ERROR_MESSAGE}"}

def test_list_used_variables():
    assert _results(LIST_USED_VARIABLES) == set()

def test_used_after_loop():
    assert _results(USED_AFTER_LOOP) == {f"2:1 {ERROR_MESSAGE}"}

def test_long_for_loop():
    assert _results(LONG_FOR_LOOP) == set()

def test_redefined_unused_variable():
    assert _results(REDEFINED_UNUSED_VARIABLE) == {f"2:1 {ERROR_MESSAGE}"}

def test_redefined_unused_variable_in_loop():
    assert _results(REDEFINED_UNUSED_VARIABLE_IN_LOOP) == {f"2:1 {ERROR_MESSAGE}"}

def test_redefined_used_variable():
    assert _results(REDEFINED_USED_VARIABLE) == set()

def test_redefined_unused_in_complicated_structure():
    assert _results(REDEFINED_UNUSED_IN_COMPLICATED_STRUCTURE) == {f"2:1 {ERROR_MESSAGE}"}

def test_underscore_variable():
    assert _results(UNDERSCORE_VARIABLE) == set()

def test_nested_for_loops():
    assert _results(NESTED_FOR_LOOPS) == {f"2:1 {ERROR_MESSAGE}"}
