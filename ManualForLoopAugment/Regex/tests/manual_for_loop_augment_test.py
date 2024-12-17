from manual_for_loop_augment import find_misconception

TRIVIAL_CASE = """
for i in range(10):
    print(i)
"""

REASSIGNMENT = """
for i in range(10):
    print(i)
    i = i + 1
    print(i)
"""

AUGMENT = """
for i in range(10):
    print(i)
    print(i)
    i += 1
"""

WEIRD_1 = """
for   hey    in   [  1 ,    2,  3   ]   :
    print(   hey  )
    hey    +=    3
"""

WEIRD_2 = """
for    yeh    in    function(1 ,  'a',   test.legs)   :
    if yeh < _wey:
        print(yeh)
    yeh += _wey
"""

def test_trivial_case():
    assert not find_misconception(TRIVIAL_CASE)

def test_reassignment():
    assert find_misconception(REASSIGNMENT)

def test_augment():
    assert find_misconception(AUGMENT)

def test_weird_1():
    assert find_misconception(WEIRD_1)

def test_weird_2():
    assert find_misconception(WEIRD_2)
