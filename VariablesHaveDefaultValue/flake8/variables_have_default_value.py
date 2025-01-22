import ast
from typing import Generator, Tuple, Type, Any, List
import builtins

ERROR_MESSAGE = "VDV Variables don't have default values, they must be defined before being used"

class Visitor(ast.NodeVisitor):
    def __init__(self) -> None:
        self.problems: List[Tuple[int, int]] = []
        self.defined_variables: List[str] = []
        self.defined_arguments: List[str] = []

    def get_problems(self):
        return self.problems
    
    def visit_Assign(self, node: ast.Assign):
        self.generic_visit(node)
        for target in node.targets:
            if isinstance(target, ast.Name):
                self.defined_variables.append(target.id)

    def visit_For(self, node: ast.For):
        if isinstance(node.target, ast.Name):
            self.defined_variables.append(node.target.id)
        self.generic_visit(node)

    def visit_FunctionDef(self, node: ast.FunctionDef):
        self.defined_arguments = [argument.arg for argument in node.args.args]
        self.defined_variables.append(node.name)
        self.generic_visit(node)
        self.defined_arguments = []

    def visit_Name(self, node: ast.Name):
        if isinstance(node.ctx, ast.Load) \
        and node.id not in self.defined_variables \
        and node.id not in self.defined_arguments:
            try:
                getattr(builtins, node.id)
            except AttributeError:
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
