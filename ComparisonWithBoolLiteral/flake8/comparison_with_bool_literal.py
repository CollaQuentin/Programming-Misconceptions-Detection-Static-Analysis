import ast
from typing import Generator, Tuple, Type, Any, List

ERROR_MESSAGE = "CWB Comparing an expression to True|False is not necessary"


class Visitor(ast.NodeVisitor):
    def __init__(self) -> None:
        self.problems: List[Tuple[int, int]] = []

    def get_problems(self) -> List[Tuple[int, int]]:
        return self.problems

    def visit_Compare(self, node: ast.Compare) -> None:
        if (
            (isinstance(node.left, ast.Constant)
                and (node.left.value is True or node.left.value is False))
            or any(isinstance(comp, ast.Constant)
                   and (comp.value is True or comp.value is False)
                   for comp in node.comparators)
        ):
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
