from map_to_boolean_with_to import find_misconception

TRIVIAL_CASE = """
x = 5
is_greater_than_10 = x > 10
"""

MAP_TO_BOOLEAN_WITH_TO = """
x = 5
is_greater_than_10 = True if x > 10 else False
"""

MAP_TO_BOOLEAN_WITH_TO_RETURN = """
def is_greater_than_5(x):
    return True if x > 5 else False
"""

def test_trivial_case():
    assert not find_misconception(TRIVIAL_CASE)

def test_map_to_boolean_with_to():
    assert find_misconception(MAP_TO_BOOLEAN_WITH_TO)

def test_map_to_boolean_with_to_return():
    assert find_misconception(MAP_TO_BOOLEAN_WITH_TO_RETURN)


