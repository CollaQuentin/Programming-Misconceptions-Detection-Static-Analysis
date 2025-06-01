from useless_for_loop_range import find_misconception

TRIVIAL_CASE = """
l = [1, 2, 3, 4, 5]
for x in l:
    print(x)
"""

USELESS_FOR_LOOP_RANGE = """
l = [1, 2, 3, 4, 5]
for i in range(len(l)):
    print(l[i])
"""

USEFUL_FOR_LOOP_RANGE = """
l = [1, 2, 3, 4, 5]
for i in range(len(l)):
    print(i)
    l[i] = 0
"""

def test_trivial_case():
    assert not find_misconception(TRIVIAL_CASE)

def test_useless_for_loop_range():
    assert find_misconception(USELESS_FOR_LOOP_RANGE)

def test_useful_For_loop_range():
    assert not find_misconception(USEFUL_FOR_LOOP_RANGE)