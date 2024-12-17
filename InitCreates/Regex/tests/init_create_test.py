from init_create import find_misconception

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

CREATES_OBJECT = """
class Dog:
    def __init__(self, name):
        self.name = name
        dog = Dog(name)

    def bark(self):
        print("Woof !")
"""

CREATES_OBJECT_NESTED = """
class Dog:
    def __init__(self, name):
        self.name = name
        if name.endswith("new"):
            if len(name) == 3:
                dog = Dog(name)
"""

CREATES_OTHER_OBJECT = """
class Dog:
    def __init__(self, name):
        self.name = name

class Human:
    def __init__(self, name, pet_name):
        self.name = name
        self.pet = Dog(pet_name)
"""

def test_trivial_case():
    assert not find_misconception(TRIVIAL_CASE)

def test_no_init():
    assert not find_misconception(NO_INIT)

def test_creates_object():
    assert find_misconception(CREATES_OBJECT)

def test_creates_object_nested():
    assert find_misconception(CREATES_OBJECT_NESTED)

def test_creates_other_object():
    assert not find_misconception(CREATES_OTHER_OBJECT)