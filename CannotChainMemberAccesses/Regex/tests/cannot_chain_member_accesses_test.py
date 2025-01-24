from cannot_chain_member_accesses import find_misconception

TRIVIAL_CASE = """
print(node.next.value)
"""

CANNOT_CHAIN_MEMBER_ACCESSES = """
n = node.next
print(node.value)
"""

def test_trivial_case():
    assert not find_misconception(TRIVIAL_CASE)

def test_cannot_chain_member_accesses():
    assert find_misconception(CANNOT_CHAIN_MEMBER_ACCESSES)