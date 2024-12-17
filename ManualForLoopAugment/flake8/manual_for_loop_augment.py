import ast
from typing import Generator, Tuple, Type, Any, List, Dict

ERROR_MESSAGE = "MFA There's no need to increment the for loop variable"


class ParentTracking(ast.NodeVisitor):
    def __init__(self):
        self.parents: Dict[ast.AST : ast.AST] = {}

    def visit(self, node: ast.AST):
        for child in ast.iter_child_nodes(node):
            self.parents[child] = node
        super().visit(node)

    def get_parent(self, node: ast.AST) -> ast.AST:
        return self.parents.get(node, None)
    
    def get_parents(self, node: ast.AST) -> Generator[ast.AST, None, None]:
        climber = node
        while (climber := self.get_parent(climber)) is not None:
            yield climber

    def is_child_of(self, child: ast.AST, parent: ast.AST) -> bool:
        for node in self.get_parents(child):
            if node == parent:
                return True
        return False


class Visitor(ParentTracking):
    def __init__(self) -> None:
        super().__init__()
        self.problems: List[Tuple[int, int]] = []
        self.for_loops: Dict[ast.For:List[ast.Name]] = {}

    def visit_For(self, node: ast.For) -> None:
        if isinstance(node.target, ast.Name):
            self.for_loops[node] = [node.target]
        elif isinstance(node.target, ast.Tuple) or isinstance(node.target, ast.List):
            self.for_loops[node] = node.target
        self.generic_visit(node)

    def visit_Assign(self, node: ast.Assign) -> None:
        for for_loop, variables in self.for_loops.items():
            if self.is_child_of(node, for_loop):  # assign in a for loop
                for target in node.targets:
                    if any(variable.id == target.id for variable in variables):
                        self.problems.append((node.lineno, node.col_offset))
                        break  # don't look at the other variables
        self.generic_visit(node)

    def visit_AugAssign(self, node: ast.AugAssign) -> None:
        for for_loop, variables in self.for_loops.items():
            if self.is_child_of(node, for_loop):
                if any(variable.id == node.target.id for variable in variables):
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
