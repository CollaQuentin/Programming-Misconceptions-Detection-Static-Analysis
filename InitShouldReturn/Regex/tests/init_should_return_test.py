from init_should_return import find_misconception

TRIVIAL_CASE = """
class Dog:
    def __init__(self, name):
        self.name = name

    def get_name(self):
        return self.name

    def bark(self):
        print("Woof !")
"""

NO_INIT = """
class Dog:
    def bark(self):
        print("Woof !")
"""

SIMPLE_RETURN = """
class Dog:
    def __init__(self):
        return 0
"""

RETURN_CLASSNAME = """
class Dog:
    def __init__(self):
        return Dog()

    def bark(self):
        print("Woof !")
"""

RETURN_AFTER_ATTRIBUTES = """
class Dog:
    def __init__(self, name):
        self.name = name
        return self
"""



def test_trivial_case():
    assert not find_misconception(TRIVIAL_CASE)

def test_no_init():
    assert not find_misconception(NO_INIT)

def test_simple_return():
    assert find_misconception(SIMPLE_RETURN)

def test_return_classname():
    assert find_misconception(RETURN_CLASSNAME)

def test_return_after_attributes():
    assert find_misconception(RETURN_AFTER_ATTRIBUTES)