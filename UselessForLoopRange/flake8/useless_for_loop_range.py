import ast
from typing import Generator, Tuple, Type, Any, List, Dict
from dataclasses import dataclass

ERROR_MESSAGE = "UFR It is not always necessary to iterate over the index of a list. Consider iterating over the items directly."

@dataclass
class ForLoop:
    target: str
    iter: str
    was_useful_indexing: bool = False

def get_loop_info(loop: ast.For) -> ForLoop:
    if not isinstance(loop.target, ast.Name):
        return None
    target = loop.target.id
    if isinstance(loop.iter, ast.Call) and loop.iter.func.id == "range":
        for arg in loop.iter.args:   # range arguments
            if isinstance(arg, ast.Call) and arg.func.id == "len" \
            and isinstance(arg.args[0], ast.Name):
                iter = arg.args[0].id
                return ForLoop(target, iter)
    return None

class Visitor(ast.NodeVisitor):
    def __init__(self) -> None:
        self.problems: List[Tuple[int, int]] = []
        self.for_loops: List[ForLoop] = []

    def get_problems(self):
        return self.problems
    
    def visit_For(self, node: ast.For):
        if loop := get_loop_info(node):
            self.for_loops.append(loop)
        self.generic_visit(node)
        if loop and not loop.was_useful_indexing:
            self.problems.append((node.lineno, node.col_offset))

    def visit_Subscript(self, node: ast.Subscript):
        if isinstance(node.ctx, ast.Store):
            for loop in self.for_loops:
                if loop.target == node.slice.id:
                    loop.was_useful_indexing = True
                break
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
