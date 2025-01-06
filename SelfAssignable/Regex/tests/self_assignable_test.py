from self_assignable import find_misconception

TRIVIAL_CASE = """
def __init__(self, name):
    self.name = name
"""

SELF_ASSIGNED = """
def __init__(self, name):
    self = name
"""

def test_trivial_case():
    assert not find_misconception(TRIVIAL_CASE)

def test_self_assigned():
    assert find_misconception(SELF_ASSIGNED)