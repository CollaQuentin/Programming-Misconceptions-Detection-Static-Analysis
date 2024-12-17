import ast
from typing import Generator, Tuple, Type, Any, List

ERROR_MESSAGE = "ISR An init method should not return anything"


def is_init_method(statement: ast.stmt):
    return (
        isinstance(statement, ast.FunctionDef) and
        statement.name == '__init__'
    )

class Visitor(ast.NodeVisitor):
    def __init__(self) -> None:
        self.problems: List[Tuple[int, int]] = []

    def visit_FunctionDef(self, node: ast.FunctionDef) -> None:
        if node.name == '__init__':
            if any(isinstance(stmt, ast.Return) for stmt in node.body):
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
