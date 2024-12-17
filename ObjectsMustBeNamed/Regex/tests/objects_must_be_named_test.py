from objects_must_be_named import find_misconception

TRIVIAL_CASE = """
d = Dog("Steve")
d.bark()
print(f"My dog is named {d.name} :)")
"""

USELESS_INSTANCE = """
d = Dog("Steve")
d.bark()
"""

ONE_LINER = """
Dog("Steve").bark()
"""

USELESS_INT_STORAGE = """
a = 1
print(a)
"""

USEFUL_INT_STORAGE = """
a = 1
a += 3
print(a)
"""

def test_trivial_case():
    assert not find_misconception(TRIVIAL_CASE)

def test_useless_instance():
    assert find_misconception(USELESS_INSTANCE)

def test_one_liner():
    assert not find_misconception(ONE_LINER)

def test_useless_int_storage():
    assert find_misconception(USELESS_INT_STORAGE)

def test_useful_int_storage():
    assert not find_misconception(USEFUL_INT_STORAGE)
