import ast
from typing import Generator, Tuple, Type, Any, List

ERROR_MESSAGE = "DR Statements after a return will never be executed"

def find_deferred_return(block: List[ast.stmt]):
    problems = []
    for index, statement in enumerate(block):
        if isinstance(statement, ast.If | ast.While | ast.For | ast.Try | ast.With):
            problems.extend(find_deferred_return(statement.body))
        if isinstance(statement, ast.Return) and index != len(block) - 1:
            problems.extend(
                (further_statement.lineno, further_statement.col_offset)
                for further_statement in block[index+1:]
            )
            break
    return problems


class Visitor(ast.NodeVisitor):
    def __init__(self) -> None:
        self.problems: List[Tuple[int, int]] = []

    def get_problems(self):
        return self.problems

    def visit_FunctionDef(self, node: ast.FunctionDef):
        self.problems.extend(find_deferred_return(node.body))
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
