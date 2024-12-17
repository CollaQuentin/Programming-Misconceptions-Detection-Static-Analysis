from no_empty_init import find_misconception

TRIVIAL_CASE = """
class Dog:
    def __init__(self, name, legs):
        self.name = name
        self.legs = legs

    def get_name(self):
        return self.name

    def get_legs(self):
        return self.legs
"""

RETURN_NONE = """
class Dog:
    def __init__(self):
        return None
"""

PASS = """
class Dog:
    def __init__(self, name, legs):
        pass
"""

ELLIPSIS = """
class Dog:
    def __init__(self, name, legs):
        ...
"""

DOCSTRING = """
class Dog:
    def __init__(self, name, legs):
        \"\"\"
        This is a docstring
        \"\"\"

    def bark(self):
        print("Woof")
"""

DOCSTRING_WITH_RETURN = """
class Dog:
    def __init__(self, name, legs):
        \"\"\"
        This is a docstring
        \"\"\"
        return
"""

def test_trivial_case():
    assert not find_misconception(TRIVIAL_CASE)

def test_return_none():
    assert find_misconception(RETURN_NONE)

def test_pass():
    assert find_misconception(PASS)

def test_ellipsis():
    assert find_misconception(ELLIPSIS)

def test_docstring():
    assert find_misconception(DOCSTRING)

def test_docstring_with_return():
    assert find_misconception(DOCSTRING_WITH_RETURN)