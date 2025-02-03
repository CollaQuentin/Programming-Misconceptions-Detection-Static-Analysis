import python

from Delete del
where exists(Name n | n = del.getATarget() | n.toString() = "self")
select del, del.getLocation().getFile().getShortName()
