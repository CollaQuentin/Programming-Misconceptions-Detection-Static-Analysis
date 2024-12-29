from assign_compares import find_misconception

TRIVIAL_CASE = """
x = 1
while x <= 10:
    print(x)
    x += 1
"""

INCORRECT_IF = """
x = 1
if x = 1:
    print("x is one")
"""

INCORRECT_WHILE = """
condition = True
while condition = True:
    print("The condition is true")
"""

NESTED_IF = """
x = 1
condition = True
if condition:
    if x = 1:
        print("x is still one")
"""

NESTED_WHILE = """
x = 1
condition = True
if condition:
    while x = 1:
        print("x is still one")
"""

CORRECT_IF = """
x = 1
if x == 1:
    print("x is one")
"""

CORRECT_WHILE = """
x = 0
while x != 10:
    print(x)
    x += 1
"""

PARENTHESES = """
x = 0
if ( x = 0):
    print("x is zero")
"""

# The following comment was found in a student's submission (6578c6c0c6b05849cef3406b)
WITH_COMMENT = """
# Demander à l'utilisateur d'entrer un entier strictement positif s0 = int(input("Entrez un entier strictement positif (s0) : "))
x = 0:
    if x == 0:
        print("x is 0")
"""

# 65154a4b53046160bca53ca0
EMPTY_IF = """
s0=5
print(s0)
while(s0!=0):
   if
      s0=s0/2
   else:
      s0=3*s0+1
   print(s0)
"""

def test_trivial_case():
    assert not find_misconception(TRIVIAL_CASE)

def test_incorrect_if():
    assert find_misconception(INCORRECT_IF)

def test_incorrect_while():
    assert find_misconception(INCORRECT_WHILE)

def test_nested_if():
    assert find_misconception(NESTED_IF)

def test_nested_while():
    assert find_misconception(NESTED_WHILE)

def test_correct_if():
    assert not find_misconception(CORRECT_IF)

def test_correct_while():
    assert not find_misconception(CORRECT_WHILE)

def test_parentheses():
    assert find_misconception(PARENTHESES)

def test_with_comment():
    assert not find_misconception(WITH_COMMENT)

def test_empty_if():
    assert not find_misconception(EMPTY_IF)