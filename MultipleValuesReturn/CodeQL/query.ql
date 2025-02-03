import python

from Return r
where r.getValue() instanceof Tuple 
    and not r.getValue().isParenthesized()
select r, r.getLocation().getFile().getShortName()
