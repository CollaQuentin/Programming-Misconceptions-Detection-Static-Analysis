import ast
from typing import Generator, Tuple, Type, Any, List

ERROR_MESSAGE = "NAM It is not always necessary to iterate over the index of a list. Consider iterating over the items directly."

def is_self_attribute(target: ast.Name | ast.Attribute | ast.Tuple) -> bool:
    return (isinstance(target, ast.Attribute) 
            and isinstance(target.value, ast.Name)
            and target.value.id == "self")
    

def get_class_attributes_from_init_method(init_method: ast.FunctionDef) -> List[str]:
    attributes: List[str] = []
    for stmt in init_method.body:
        if isinstance(stmt, ast.Assign):
            for target in stmt.targets:
                if is_self_attribute(target):
                    attributes.append(target.attr)
    return attributes

class Visitor(ast.NodeVisitor):
    def __init__(self) -> None:
        self.problems: List[Tuple[int, int]] = []
        self.init_attributes: List[str] = []
        self.visiting_class: bool = False
        self.visiting_method: str = None

    def get_problems(self):
        return self.problems
    
    def visit_ClassDef(self, node: ast.ClassDef):
        self.visiting_class = True
        self.generic_visit(node)
        self.visiting_class = False
        self.init_attributes = []

    def visit_FunctionDef(self, node: ast.FunctionDef):
        if self.visiting_class:
            self.visiting_method = node.name
        self.generic_visit(node)
        self.visiting_method = None

    def visit_Assign(self, node: ast.Assign):
        if self.visiting_method:
            if self.visiting_method == "__init__":
                for target in node.targets:
                    if is_self_attribute(target):
                        self.init_attributes.append(target.attr)
            else:
                for target in node.targets:
                    if is_self_attribute(target) and not target.attr in self.init_attributes:
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
