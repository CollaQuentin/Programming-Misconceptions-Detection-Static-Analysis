import ast
from typing import Generator, Tuple, Type, Any, List

ERROR_MESSAGE = "IC The __init__ method is not supposed to create a new object in its body"

class Visitor(ast.NodeVisitor):
    def __init__(self) -> None:
        self.problems: List[Tuple[int, int]] = []
        self.visiting_class: str = None
        self.visiting_init: ast.FunctionDef = None

    def get_problems(self) -> List[Tuple[int, int]]:
        return self.problems

    def visit_ClassDef(self, node) -> None:
        self.visiting_class = node.name
        self.generic_visit(node)

    def visit_FunctionDef(self, node) -> None:
        if node.name == "__init__":
            self.visiting_init = node
        self.generic_visit(node)
        self.visiting_init = None

    def visit_Call(self, node) -> None:
        if (
            isinstance(node.func, ast.Name)
            and self.visiting_init
            and node.func.id == self.visiting_class
        ):
            self.problems.append(
                (self.visiting_init.lineno, self.visiting_init.col_offset)
            )
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
