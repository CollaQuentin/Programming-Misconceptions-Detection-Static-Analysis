from wasted_return_value import find_misconception

TRIVIAL_CASE = """
def foo(bar):
    return -bar

print(foo(5))
"""

STORED_RETURN = """
def foo(bar):
    return -bar

opposite = foo(5)
"""

RETURN = """
def foo(bar):
    return

foo(5)
"""

WASTED_RETURN_VALUE = """
def foo(bar):
    return -bar

foo(5)
"""

TEST = """
def rho(a,b,c):
    return b**2 - 4*a*c

def n_solutions(a,b,c):
    if rho(a,b,c) > 0 :
        return 2
    elif rho(a,b,c) == 0 :
        return 1
    else :
        return 0
def solution(a,b,c):
    if n_solutions(a,b,c) > 1 :
        if a > 0:
            return (-b - math.sqrt(rho(a, b, c)))/(2*a)
        else:
            return (-b + math.sqrt(rho(a, b, c)))/(2*a)
    elif n_solutions(a, b, c) == 1:
        return (-b+rho(a, b, c))/(2*a)
    else:
        return None
"""

TEST2 = """
def rho(a,b,c):
    return (b**2)-(4*a*c)

def n_solutions(a,b,c):
    if rho(a,b,c) == 0:
        return 1
    elif rho(a,b,c) > 0:
        return 2
    else:
        return 0

def solution(a,b,c):
    if rho(a,b,c) == 0:
        return -b/(2*a)

    elif rho(a,b,c):
        x = (-b+racine_carree(rho(a,b,c)))/2*a
        y = (-b-racine_carree(rho(a,b,c)))/2*a
        if x<y:
            return x
        else:
            return y
"""

def test_trivial_case():
    assert not find_misconception(TRIVIAL_CASE)

def test_stored_return():
    assert not find_misconception(STORED_RETURN)

def test_return():
    assert not find_misconception(RETURN)

def test_wasted_return_value():
    assert find_misconception(WASTED_RETURN_VALUE)

def test_test():
    assert not find_misconception(TEST)

def test_test2():
    assert not find_misconception(TEST2)