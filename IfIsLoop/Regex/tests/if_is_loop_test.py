from if_is_loop import find_misconception

TRIVIAL_CASE = """
if x < 10:
    print("x is smaller than 10")
    min = x
"""

IF_IS_LOOP = """
if x < 10:
    x += 1
    print(x)
"""

def test_trivial_case():
    assert not find_misconception(TRIVIAL_CASE)

def test_if_is_loop():
    assert find_misconception(IF_IS_LOOP)



