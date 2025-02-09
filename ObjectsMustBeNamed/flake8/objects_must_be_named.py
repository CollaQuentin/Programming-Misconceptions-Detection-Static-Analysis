import ast
from dataclasses import dataclass
from typing import Generator, Tuple, Type, Any, List

ERROR_MESSAGE = "OMN Variable \"{}\" is used only once"
MIN_USAGE_REQUIRED = 2  # If used less than twice, the value didn't have to be stored

# a = 1
# print(a)    <- first (and last) usage
#
# Could have been replaced by 
#
# print(1)

def get_names_from_List(l: ast.List | ast.Tuple) -> List[ast.Name]:
    ids = []
    for assignment in l.elts:
        if isinstance(assignment, ast.Name):
            ids.append(assignment)
        elif isinstance(assignment, ast.List | ast.Tuple):
            ids.extend(get_names_from_List(assignment))
    return ids

def get_assign_targets(node: ast.Assign) -> List[ast.Name]:
    for target in node.targets:
        if isinstance(target, ast.Attribute): continue
        names = [target] if isinstance(target, ast.Name) \
                else get_names_from_List(target)
        return names

def get_assign_targets(node: ast.Assign) -> List[ast.Name]:
    names = []
    for target in node.targets:
        if isinstance(target, ast.Attribute): continue
        if isinstance(target, ast.Name):
            names.append(target)
        else:
            names.extend(get_names_from_List(target))
    return names

@dataclass
class Variable:
    name: str
    usage: int
    loop: ast.For | ast.While
    lineno: int
    col_offset: int

    def __str__(self):
        return f"[{self.lineno}:{self.col_offset}] {self.name} ({self.usage})"


class Visitor(ast.NodeVisitor):
    def __init__(self):
        self.problems: List[Tuple[str, int, int]] = []
        self.variables: List[Variable] = []
        
        self.current_assignment_targets: List[str] = []
        self.current_loops: List[ast.For|ast.While] = [None]

    def get_problems(self):
        for problem in self.problems:
            yield problem
        for variable in self.variables:
            if variable.usage < MIN_USAGE_REQUIRED:
                yield (variable.name, variable.lineno, variable.col_offset)

    def get_current_loop(self):
        return self.current_loops[-1]

    def visit_For(self, node: ast.For):
        if isinstance(node.target, ast.Name):
            for variable in self.variables:
                if variable.name == node.target.id and variable.usage < MIN_USAGE_REQUIRED:
                    self.problems.append((variable.name, variable.lineno, variable.col_offset))
                self.variables = list(filter(lambda x:x.name != node.target.id, self.variables))
        self.current_loops.append(node)
        self.generic_visit(node)
        self.current_loops.pop()

    def visit_While(self, node: ast.While):
        self.current_loops.append(node)
        self.generic_visit(node)
        self.current_loops.pop()
    
    def visit_Assign(self, node: ast.Assign):
        targets = get_assign_targets(node)
        self.problems.extend(
            (v.name, v.lineno, v.col_offset)
            for v in self.variables
            if any(v.name == name.id for name in targets) and v.usage < MIN_USAGE_REQUIRED
        )
        self.variables = list(filter(lambda var: all(name.id != var.name for name in targets), self.variables))
        for name in targets:
            self.variables.append(Variable(name.id, 0, self.get_current_loop(), name.lineno, name.col_offset))
        self.current_assignment_targets = [target.id for target in targets]
        self.generic_visit(node)
        self.current_assignment_targets = []

    def visit_Name(self, node: ast.Name):
        if node.id in self.current_assignment_targets:
            self.generic_visit(node)
            return
        for variable in self.variables:
            if variable.name == node.id:
                if self.get_current_loop() == variable.loop:
                    variable.usage += 1
                else:
                    # print(f"{variable} usage +2")
                    variable.usage += MIN_USAGE_REQUIRED  # If a variable is used in a loop, the misconception does not trigger
        self.generic_visit(node)

class Plugin:
    name = __name__
    version = "0.1.0"

    def __init__(self, tree: ast.AST) -> None:
        self._tree = tree

    def run(self) -> Generator[Tuple[int, int, str, Type[Any]], None, None]:
        visitor = Visitor()
        visitor.visit(self._tree)
        for var_name, line, col in visitor.get_problems():
            # print(var_name, line, col)
            yield line, col, ERROR_MESSAGE.format(var_name), type(self)
