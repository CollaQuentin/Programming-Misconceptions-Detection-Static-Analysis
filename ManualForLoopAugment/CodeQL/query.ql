import python

from For loop
where 
    exists(
        Assign a | a.getTarget(0).(Name).getId() = loop.getTarget().(Name).getId()
        and loop.getBody().contains(a)
    )
    or exists(
        AugAssign a | a.getTarget().(Name).getId() = loop.getTarget().(Name).getId()
        and loop.getBody().contains(a)
    )
select loop, loop.getLocation().getFile().getShortName(), loop.getLocation().getStartLine()
