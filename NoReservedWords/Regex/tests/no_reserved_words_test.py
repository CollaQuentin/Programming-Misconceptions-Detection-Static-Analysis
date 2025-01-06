from no_reserved_words import find_misconception

TRIVIAL_CASE = """
a = 0
def foo(bar):
    return bar + 1
print(foo(a))
"""

REDEFINED_KEYWORD = """
def as(bar):
    return bar+1
"""

def test_trivial_case():
    assert not find_misconception(TRIVIAL_CASE)

def test_redefined_keywords():
    assert find_misconception(REDEFINED_KEYWORD)
