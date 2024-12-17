from unused_for_loop_variable import find_misconception

TRIVIAL_CASE = """
for i in range(10):
    print(i)
"""

UNUSED_VARIABLE = """
for i in range(10):
    print('Hello, World !')
"""

LONG_FOR_LOOP = """
for test in [1,2,3,4,5]:
    print('Hello')
    print(l[test])
    print('World')

"""

USED_AFTER_LOOP = """
for i in range(10, 20, 2):
    print('Hello')
    if x < 10:
        print(x)
print(i)
"""

USED_NESTED_IN_LOOP = """
for var in (1, 5, 10):
    if True:
        if True:
            if True:
                d[var] = True
"""

NO_FOR_LOOP = """
print("Hello, World !")
"""

def test_trivial_case():
    assert not find_misconception(TRIVIAL_CASE)

def test_unused_variable():
    assert find_misconception(UNUSED_VARIABLE)

def test_long_for_loop():
    assert not find_misconception(LONG_FOR_LOOP)

def test_used_after_loop():
    assert find_misconception(USED_AFTER_LOOP)

def test_used_nested_in_loop():
    assert not find_misconception(USED_NESTED_IN_LOOP)

def test_no_for_loop():
    assert not find_misconception(NO_FOR_LOOP)