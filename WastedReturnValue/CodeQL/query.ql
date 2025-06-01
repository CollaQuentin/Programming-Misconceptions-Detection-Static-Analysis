import python

from FunctionDef f, Call c
where exists(Expr v, Return r | r.getValue() = v and not r.getValue() instanceof None | f.contains(r))
    and c.getFunc().toString() = f.getDefinedFunction().getName()
    and c.getLocation().getFile() = f.getLocation().getFile()
    and not (
        exists(AssignStmt a | a.contains(c)) or
        exists(Subscript s | s.contains(c)) or
        exists(Call call | call.contains(c)) or
        exists(Compare comp | comp.contains(c)) or
        exists(If i | i.contains(c)) or 
        exists(While while | while.getTest().contains(c)) or 
        exists(Return r | r.contains(c))
    )
select f.getDefinedFunction().getName(), f.getLocation().getFile().getShortName(), "test"
