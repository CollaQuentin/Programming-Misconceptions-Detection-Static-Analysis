import python

from For loop
where not exists(
    Name n | n.getId() = loop.getTarget().(Name).getId() and loop.getBody().contains(n)
)
select loop, loop.getLocation().getFile().getShortName(), loop.getLocation().getStartLine()
