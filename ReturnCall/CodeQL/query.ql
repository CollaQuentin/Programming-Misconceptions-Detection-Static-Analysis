import python

from Return r
where r.getValue().isParenthesized()
    and not r.getValue() instanceof Tuple
select r, r.getLocation().getFile().getShortName(), " "
