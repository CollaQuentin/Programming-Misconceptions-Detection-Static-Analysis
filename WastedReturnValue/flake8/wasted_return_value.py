import ast
from typing import Generator, Tuple, Type, Any, List, Dict

ERROR_MESSAGE = "WRV If a function returns something, it is better to store or use that return value."

def is_return_none(node: ast.Return) -> bool:
    if not node.value:
        return True
    if isinstance(node.value, ast.Constant) and node.value.value is None:
        return True
    return False

class Visitor(ast.NodeVisitor):
    def __init__(self) -> None:
        self.problems: List[Tuple[int, int]] = []
        self.functions_return: Dict[ast.FunctionDef:bool] = {}
        self.visiting_function: ast.FunctionDef = None
        self.is_call_useful = 0

    def get_problems(self):
        return self.problems
    
    def does_return_something(self, function_name: str) -> bool:
        for function in self.functions_return:
            if function.name == function_name:
                return self.functions_return[function]
        return False
    
    def visit_FunctionDef(self, node: ast.FunctionDef):
        self.visiting_function = node
        self.generic_visit(node)
        if node not in self.functions_return:
            self.functions_return[node] = False
        self.visiting_function = None

    def visit_Return(self, node: ast.Return):
        if not is_return_none(node):
            self.functions_return[self.visiting_function] = True
        self.is_call_useful += 1
        self.generic_visit(node)
        self.is_call_useful -= 1

    def visit_Assign(self, node: ast.Assign):
        self.is_call_useful += 1
        self.generic_visit(node)
        self.is_call_useful -= 1

    def visit_Compare(self, node: ast.Compare):
        self.is_call_useful += 1
        self.generic_visit(node)
        self.is_call_useful -= 1

    def visit_Call(self, node: ast.Call):
        if isinstance(node.func, ast.Name):
            if self.does_return_something(node.func.id) and self.is_call_useful <= 0:
                self.problems.append((node.lineno, node.col_offset))
        self.is_call_useful += 1
        self.generic_visit(node)
        self.is_call_useful -= 1


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
