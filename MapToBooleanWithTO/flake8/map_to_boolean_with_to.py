import ast
from typing import Generator, Tuple, Type, Any, List

ERROR_MESSAGE = "MBT It's not necessary to map values to boolean using a ternary operator (consider using `bool()`)"

def are_opposite_boolean(first: ast.Constant, second: ast.Constant) -> bool:
    if first.value is True:
        return second.value is False
    elif first.value is False:
        return second.value is True
    return False

class Visitor(ast.NodeVisitor):
    def __init__(self) -> None:
        self.problems: List[Tuple[int, int]] = []

    def get_problems(self):
        return self.problems
    
    def visit_IfExp(self, node: ast.IfExp):
        if isinstance(node.body, ast.Constant) and isinstance(node.orelse, ast.Constant):
            if are_opposite_boolean(node.body, node.orelse):
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
        for line, col in visitor.get_problems():
            yield line, col, ERROR_MESSAGE, type(self)
