import ast
from typing import Generator, Tuple, Type, Any, List

ERROR_MESSAGE = "NEI The init method could be empty"


def is_one_line_init(statement: ast.stmt) -> bool:
    return (
        isinstance(statement, ast.FunctionDef) and
        statement.name == '__init__' and
        len(statement.body) == 1
    )


def is_useless_statement(statement: ast.stmt) -> bool:
    return (
        isinstance(statement, ast.Pass) or
        (isinstance(statement, ast.Return) and isinstance(statement.value, ast.Constant) and statement.value.value is None) or
        (
            isinstance(statement, ast.Expr) and
            isinstance(statement.value, ast.Constant) and
            (
                isinstance(statement.value.value, str) or  # Docstring
                statement.value.value == ...               # Ellipsis
            )
        )

    )

class Visitor(ast.NodeVisitor):
    def __init__(self) -> None:
        self.problems: List[Tuple[int, int]] = []

    def visit_ClassDef(self, node: ast.ClassDef) -> None:
        for stmt in node.body:
            if is_one_line_init(stmt):
                lineno = stmt.lineno
                col_offset = stmt.col_offset
                statement = stmt.body[0]
                if is_useless_statement(statement):
                    self.problems.append((lineno, col_offset))
        self.generic_visit(node)

class Plugin:
    name = __name__
    version = "0.1.0"

    def __init__(self, tree: ast.AST) -> None:
        self._tree = tree

    def run(self) -> Generator[Tuple[int, int, str, Type[Any]], None, None]:
        visitor = Visitor()
        visitor.visit(self._tree)
        # Add useless assignments' lineno and col_offset to the problems
        for line, col in visitor.problems:
            yield line, col, ERROR_MESSAGE, type(self)
