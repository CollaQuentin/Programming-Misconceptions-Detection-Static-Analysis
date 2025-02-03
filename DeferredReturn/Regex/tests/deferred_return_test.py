from deferred_return import find_misconception

TRIVIAL_CASE = """
def foo(bar):
    print("This is before the return")
    if bar > 5:
        print("This is in the condition")
        return bar
    print("This is after the condition")
    return bar
"""

DEFERRED_RETURN = """
def foo(bar):
    if bar > 5:
        return bar
        print("This will never print")
    return bar
"""

SHORT_FUNCTION = """
def foo(bar):
    return bar
    print(bar)
"""

def test_trivial_case():
    assert not find_misconception(TRIVIAL_CASE)

def test_deferred_return():
    assert find_misconception(DEFERRED_RETURN)

def test_short_function():
    assert find_misconception(SHORT_FUNCTION)