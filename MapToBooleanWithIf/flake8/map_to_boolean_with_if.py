import ast
from typing import Generator, Tuple, Type, Any, List

ERROR_MESSAGE = "MBI It's not necessary to map values to boolean using `if` (consider using `bool()`)"

def same_target(first_assign: ast.Assign, second_assign: ast.Assign):
    if not len(first_assign.targets) == len(second_assign.targets) == 1:
        return False
    if not (isinstance(first_assign.targets[0], ast.Name) and isinstance(second_assign.targets[0], ast.Name)):
        return False
    return first_assign.targets[0].id == second_assign.targets[0].id


def return_opposite_booleans(first: ast.stmt, second: ast.stmt):
    if not (isinstance(first, ast.Return) and isinstance(second, ast.Return)):
        return False
    if not (isinstance(first.value, ast.Constant) and isinstance(second.value, ast.Constant)):
        return False
    return first.value.value ^ second.value.value  # xor

def assign_opposite_booleans(first: ast.stmt, second: ast.stmt):
    if not (isinstance(first, ast.Assign) and isinstance(second, ast.Assign)):
        return False
    if not same_target(first, second):
        return False
    if not (isinstance(first.value, ast.Constant) and isinstance(second.value, ast.Constant)):
        return False
    return first.value.value ^ second.value.value 


class Visitor(ast.NodeVisitor):
    def __init__(self):
        self.problems: List[Tuple[int, int]] = []
        
    def visit_If(self, node: ast.If):
        if len(node.orelse) == len(node.body) == 1:
            stmt1, stmt2 = node.body[0], node.orelse[0]
            if return_opposite_booleans(stmt1, stmt2) or assign_opposite_booleans(stmt1, stmt2):
                self.problems.append((node.lineno, node.col_offset))
        self.generic_visit(node)

class Plugin:
    name = __name__
    version = "0.1.0"

    def __init__(self, tree: ast.AST) -> None:
        self._tree = tree

    def run(self) -> Generator[Tuple[int, int, str, Type[Any]], None, None]:
        visitor = Visitor()
        visitor.visit(self._tree)
        for line, col in visitor.problems:
            yield line, col, ERROR_MESSAGE, type(self)
