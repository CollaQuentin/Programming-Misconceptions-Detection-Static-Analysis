import ast
from typing import Generator, Tuple, Type, Any, List, Set

ERROR_MESSAGE = "IIL The body of an `if` statement is only executed once, consider using `while`"

def get_condition_members(if_node: ast.If) -> List[str]:
    members = []
    if not isinstance(if_node.test, ast.Compare):
        return members
    if isinstance(if_node.test.left, ast.Name):
        members.append(if_node.test.left.id)
    for comparator in if_node.test.comparators:
        if isinstance(comparator, ast.Name):
            members.append(comparator.id)
    return members


class Visitor(ast.NodeVisitor):
    def __init__(self) -> None:
        self.problems: Set[Tuple[int, int]] = set()

    def get_problems(self):
        return self.problems
    
    def visit_If(self, node: ast.If):
        members: List[str] = get_condition_members(node)
        for stmt in node.body:
            if isinstance(stmt, ast.Assign):
                for target in stmt.targets:
                    if isinstance(target, ast.Name) and target.id in members:
                        self.problems.add((node.lineno, node.col_offset))
            elif isinstance(stmt, ast.AugAssign):
                if isinstance(stmt.target, ast.Name) and stmt.target.id in members:
                    self.problems.add((node.lineno, node.col_offset))
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
