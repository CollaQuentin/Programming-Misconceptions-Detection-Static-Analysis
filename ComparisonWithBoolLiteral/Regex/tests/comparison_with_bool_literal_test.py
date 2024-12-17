from comparison_with_bool_literal import find_misconception

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

def test_trivial_case():
    assert not find_misconception(TRIVIAL_CASE)

def test_compare_to_bool_literal():
    assert find_misconception(COMPARE_TO_BOOL_LITERAL)

def test_true_leftside_equal():
    assert find_misconception(TRUE_LEFTSIDE_EQUAL)

def test_true_righttside_equal():
    assert find_misconception(TRUE_RIGHTSIDE_EQUAL)

def test_false_leftside_equal():
    assert find_misconception(FALSE_LEFTSIDE_EQUAL)

def test_false_rightside_equal():
    assert find_misconception(FALSE_RIGHTSIDE_EQUAL)

def test_true_leftside_notequal():
    assert find_misconception(TRUE_LEFTSIDE_NOTEQUAL)

def test_true_rightside_notequal():
    assert find_misconception(TRUE_RIGHTSIDE_NOTEQUAL)

def test_false_leftside_notequal():
    assert find_misconception(FALSE_LEFTSIDE_NOTEQUAL)

def test_int_compare():
    assert not find_misconception(INT_COMPARE)

def test_false_rightside_notequal():
    assert find_misconception(FALSE_RIGHTSIDE_NOTEQUAL)
