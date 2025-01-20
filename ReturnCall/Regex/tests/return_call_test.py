from return_call import find_misconception

TRIVIAL_CASE = """
def foo(bar):
    return bar
"""

RETURN_CALL = """
def foo(bar):
    return (bar)
"""

NO_SPACE = """
def foo(bar):
    return(bar)
"""

RETURN_EXPRESSION = """
def foo(bar):
    return (1*2) + (foo * 3)
"""

def test_trivial_case():
    assert not find_misconception(TRIVIAL_CASE)

def test_return_call():
    assert find_misconception(RETURN_CALL)

def test_no_space():
    assert find_misconception(NO_SPACE)

def test_return_expression():
    assert not find_misconception(RETURN_EXPRESSION)

