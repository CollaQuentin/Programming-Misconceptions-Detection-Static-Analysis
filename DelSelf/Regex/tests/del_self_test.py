from del_self import find_misconception

TRIVIAL_CASE = """
class Dog:
    def __init__(self, name):
        self.name = name

    def bark(self):
        print("Woof !")
"""

DEL_SELF = """
class Bomb:
    def destroy(self):
        del self
"""

def test_trivial_case():
    assert not find_misconception(TRIVIAL_CASE)

def test_del_self():
    assert find_misconception(DEL_SELF)

