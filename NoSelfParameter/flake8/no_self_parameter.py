import ast
from typing import Generator, Tuple, Type, Any, List

ERROR_MESSAGE = "NSP The first parameter of a method should always be `self`"

def has_no_parameter(function_node: ast.FunctionDef) -> bool:
    return len(function_node.args.args) == 0

def first_parameter_is_self(function_node: ast.FunctionDef) -> bool:
    return function_node.args.args[0].arg == "self"

class Visitor(ast.NodeVisitor):
    def __init__(self) -> None:
        self.problems: List[Tuple[int, int]] = []
        self.visiting_class = 0

    def get_problems(self):
        return self.problems
    
    def visit_ClassDef(self, node: ast.ClassDef):
        self.visiting_class += 1
        self.generic_visit(node)
        self.visiting_class -= 1

    def currently_visiting_class(self):
        return self.visiting_class > 0

    def visit_FunctionDef(self, node: ast.FunctionDef):
        if self.currently_visiting_class():
            if has_no_parameter(node) or not first_parameter_is_self(node):
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
