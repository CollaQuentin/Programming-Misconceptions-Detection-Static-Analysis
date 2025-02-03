from map_to_boolean_with_if import find_misconception

TRIVIAL_CASE = """
a = 3
bigger_than_five = a > 5
"""

TRIVIAL_CASE_FUNCTION = """
def foo(bar):
    return bar > 5
"""

MAP_TO_BOOLEAN_IF = """
a = 3
if a > 5:
    bigger_than_five = True
else:
    bigger_than_five = False
"""

MAP_TO_BOOLEAN_RETURN = """
def foo(bar):
    if bar > 5:
        return True
    else:
        return False
"""

def test_trivial_case():
    assert not find_misconception(TRIVIAL_CASE)

def test_trivial_case_function():
    assert not find_misconception(TRIVIAL_CASE_FUNCTION)

def test_map_to_boolean_with_if():
    assert find_misconception(MAP_TO_BOOLEAN_IF)

def test_map_to_boolean_return():
    assert find_misconception(MAP_TO_BOOLEAN_RETURN)