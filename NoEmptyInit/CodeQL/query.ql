import python

predicate isDocstring(ExprStmt s) {
    exists(
        StringLiteral str | 
        s.getASubExpression() = str and str.isDocString()
    )
}

predicate isEllipsis(ExprStmt s) {
    s.getASubExpression() instanceof Ellipsis
}

from Function f
where f.isMethod()
    and f.getName() = "__init__"
    and count(f.getAStmt()) = 1
    and (
        (
            f.getAStmt() instanceof ExprStmt
            and (
                isDocstring(f.getAStmt())
                or isEllipsis(f.getAStmt())
            )
        )
        or f.getAStmt() instanceof Pass
        or f.getAStmt() instanceof Return
    )
select f, "The __init__ method is useless", f.getLocation().getFile().getShortName()