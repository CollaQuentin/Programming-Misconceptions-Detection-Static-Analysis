from multiple_values_return import find_misconception

TRIVIAL_CASE = """
def foo(bar):
    return bar
"""

RETURN_MULTIPLE_VALUES = """
def foo(a, b):
    return a, b
"""

RETURN_TUPLE = """
def foo(a,b):
    return (a, b)
"""

RETURN_MULTIPLE_VALUES_WITH_SPACES = """
def foo(a, b):
    def bar(a, b):
        return   a  , b
    return bar(a, b)
"""

def test_trivial_case():
    assert not find_misconception(TRIVIAL_CASE)

def test_return_multiple_values():
    assert find_misconception(RETURN_MULTIPLE_VALUES)

def test_return_tuple():
    assert not find_misconception(RETURN_TUPLE)

def test_return_multiple_values_with_spaces():
    assert find_misconception(RETURN_MULTIPLE_VALUES_WITH_SPACES)