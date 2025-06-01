import ast
from typing import Generator, Tuple, Type, Any, List

ERROR_MESSAGE = "CCA Member accesses can be chained"

STATEMENTS_WITH_BODY = (
    ast.FunctionDef, ast.AsyncFunctionDef,
    ast.For, ast.AsyncFor,
    ast.While,
    ast.If,
    ast.With, ast.AsyncWith,
    ast.Try, ast.TryStar
)

def is_attribute_in_value(value) -> bool:
    return isinstance(value, ast.Attribute) or (isinstance(value, ast.Call) and isinstance(value.func, ast.Attribute))


class Visitor(ast.NodeVisitor):
    def __init__(self) -> None:
        self.problems: List[Tuple[int, int]] = []
        self.current_target: str = None
        self.was_target_used: bool = False

    def get_problems(self):
        return self.problems
    
    def uses_target(self, target: str, statement: ast.stmt) -> bool:
        self.current_target = target
        if isinstance(statement, STATEMENTS_WITH_BODY):
            for name, child in ast.iter_fields(statement):
                if child \
                and name not in ("body", "orelse") \
                and not isinstance(child, STATEMENTS_WITH_BODY):
                    self.generic_visit(child)
        else:
            self.generic_visit(statement)
        if self.was_target_used:
            self.was_target_used = False
            return True
        self.current_target = None
        return False
    
    def check_for_CCA(self, body: List[ast.stmt]):
        for idx, statement in enumerate(body[:-1]):
            if isinstance(statement, ast.Assign) and is_attribute_in_value(statement.value) and isinstance(statement.targets[0], ast.Name):
                if self.uses_target(statement.targets[0].id, body[idx+1]):
                    self.problems.append((statement.lineno, statement.col_offset))

    def visit_Module(self, node: ast.Module):
        self.check_for_CCA(node.body)
        for statement in node.body:
            if isinstance(statement, STATEMENTS_WITH_BODY):
                self.check_for_CCA(statement.body)
        self.generic_visit(node)

    def visit_Name(self, node: ast.Name):
        if self.current_target and node.id == self.current_target:
            self.was_target_used = True


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
