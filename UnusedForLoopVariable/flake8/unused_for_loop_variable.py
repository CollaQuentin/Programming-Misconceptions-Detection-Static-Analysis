import ast
from typing import Generator, Tuple, Type, Any, List, Dict

ERROR_MESSAGE = "UFV A for loop variable is never used"

def get_names_from_List(l: ast.List|ast.Tuple) -> List[str]:
    ids = []
    for assignment in l.elts:
        if isinstance(assignment, ast.Name):
            ids.append(assignment.id)
        elif isinstance(assignment, ast.List|ast.Tuple):
            ids.extend(get_names_from_List(assignment))
    return ids

def get_for_loop_target_names(loop: ast.For) -> List[str]:
    if isinstance(loop.target, ast.Name):
        return [loop.target.id]
    elif isinstance(loop.target, ast.List|ast.Tuple):
        return get_names_from_List(loop.target)
    

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


class Visitor(ParentTracking):
    def __init__(self):
        super().__init__()
        self.problems: List[Tuple[int, int]] = []
                                            # List of [var_name, usage]
        self.for_loop_variables: Dict[ast.For:List[List[str, int]]] = {}

    def _remove_variable(self, for_loop: ast.For, var_name: str) -> None:
        for idx, (name, usage) in enumerate(self.for_loop_variables[for_loop]):
            if name == var_name:
                if usage < 2 and name != '_':
                    self.problems.append((for_loop.lineno, for_loop.col_offset))
                self.for_loop_variables[for_loop].pop(idx)
                break

    def yield_problems(self) -> Generator[Tuple[int, int], None, None]:
        for line, col in self.problems:
            yield line, col
        for for_loop, variables in self.for_loop_variables.items():
            for name, usage in variables:
                if usage < 2 and name != '_' :
                    yield for_loop.lineno, for_loop.col_offset
                    break

    def visit_For(self, node: ast.For) -> None:
        self.for_loop_variables[node] = [
            [name, 0] for name in get_for_loop_target_names(node)
        ]
        self.generic_visit(node)
        # if the target was not visited in the loop body, create a problem

    def visit_Name(self, node: ast.Name) -> None:
        for parent in self.get_parents(node):
            if not isinstance(parent, ast.For):
                continue
            for variable in self.for_loop_variables[parent]:
                if node.id == variable[0]:  # compare names
                    variable[1] += 1  # increment usage
        self.generic_visit(node)

    def visit_Assign(self, node: ast.Assign) -> None:
        for target in node.targets:
            if isinstance(target, ast.Attribute): continue
            names = [target.id] if isinstance(target, ast.Name) else get_names_from_List(target)
            for name in names:
                for for_loop in self.for_loop_variables.keys():
                    self._remove_variable(for_loop, name)
        self.generic_visit(node)
    

class Plugin:
    name = __name__
    version = "0.1.0"

    def __init__(self, tree: ast.AST) -> None:
        self._tree = tree

    def run(self) -> Generator[Tuple[int, int, str, Type[Any]], None, None]:
        visitor = Visitor()
        visitor.visit(self._tree)
        for line, col in visitor.yield_problems():
            yield line, col, ERROR_MESSAGE, type(self)
