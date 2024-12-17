import ast
from comparison_with_bool_literal import Plugin, ERROR_MESSAGE
from typing import Set

TRIVIAL_CASE = """
low_battery = True
if low_battery:
    print("My battery is low and it's getting dark")
"""

COMPARE_TO_BOOL_LITERAL = """
countdown = True
if countdown == True:
    print("This is the end, hold your breath and count to ten")
"""

TRUE_LEFTSIDE_EQUAL = """
stop = True
print(True == stop)
"""

TRUE_RIGHTSIDE_EQUAL = """
stop = True
print(stop == True)
"""

FALSE_LEFTSIDE_EQUAL = """
stop = False
while False == stop:
    print("This is not an infinite loop, right ?")
"""

FALSE_RIGHTSIDE_EQUAL = """
stop = False
while stop == False:
    print("RIGHT ??")
"""

TRUE_LEFTSIDE_NOTEQUAL = """
original_variable_name = True
if True != original_variable_name:
    print("I ran out of funny print ideas")
"""

TRUE_RIGHTSIDE_NOTEQUAL = """
original_variable_name = True
if True != original_variable_name:
    print("And I have two more tests to write")
"""

FALSE_LEFTSIDE_NOTEQUAL = """
x = 3
greater_than_5 = False != (x > 5)
"""

FALSE_RIGHTSIDE_NOTEQUAL = """
x = 1337
is_even = False != ~x&1
is_odd = False == (not x&1)
"""

INT_COMPARE = """
x = 3
if x == 3:
    print('X is 3 !')
"""

WHILE_TRUE = """
while True:
    print("Hello, World !")
"""

def _results(s: str) -> Set[str]:
    tree = ast.parse(s)
    plugin = Plugin(tree)
    return {f'{line}:{col+1} {msg}' for line, col, msg, _ in plugin.run()}


def test_trivial_case():
    assert _results(TRIVIAL_CASE) == set()

def test_compare_to_bool_literal():
    assert _results(COMPARE_TO_BOOL_LITERAL) == {f"3:4 {ERROR_MESSAGE}"}

def test_true_leftside_equal():
    assert _results(TRUE_LEFTSIDE_EQUAL) == {f"3:7 {ERROR_MESSAGE}"}

def test_true_rightside_equal():
    assert _results(TRUE_RIGHTSIDE_EQUAL) == {f"3:7 {ERROR_MESSAGE}"}

def test_true_leftside_notequal():
    assert _results(TRUE_LEFTSIDE_NOTEQUAL) == {f"3:4 {ERROR_MESSAGE}"}

def test_true_rightside_notequal():
    assert _results(TRUE_RIGHTSIDE_NOTEQUAL) == {f"3:4 {ERROR_MESSAGE}"}

def test_false_leftside_equal():
    assert _results(FALSE_LEFTSIDE_EQUAL) == {f"3:4 {ERROR_MESSAGE}"}

def test_false_leftside_equal():
    assert _results(FALSE_RIGHTSIDE_EQUAL) == {f"3:4 {ERROR_MESSAGE}"}

def test_false_leftside_equal():
    assert _results(FALSE_LEFTSIDE_NOTEQUAL) == {f"3:18 {ERROR_MESSAGE}"}

def test_false_leftside_equal():
    assert _results(FALSE_RIGHTSIDE_NOTEQUAL) == {
        f"3:11 {ERROR_MESSAGE}",
        f"4:10 {ERROR_MESSAGE}"
    }

def test_int_compare():
    assert _results(INT_COMPARE) == set()

def test_while_true():
    assert _results(WHILE_TRUE) == set()
