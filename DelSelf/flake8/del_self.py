import ast
from typing import Generator, Tuple, Type, Any, List

ERROR_MESSAGE = "DS There is no point in deleting `self`."

class Visitor(ast.NodeVisitor):
    def __init__(self) -> None:
        self.problems: List[Tuple[int, int]] = []

    def get_problems(self):
        return self.problems
    
    def visit_Delete(self, node: ast.Delete):
        for target in node.targets:
            if isinstance(target, ast.Name) and target.id == "self":
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
