import python

from Return r, Stmt s
where s.isUnreachable()
    and s.getLocation().getStartLine() > r.getLocation().getStartLine()
select s, s.getLocation().getFile().getShortName()