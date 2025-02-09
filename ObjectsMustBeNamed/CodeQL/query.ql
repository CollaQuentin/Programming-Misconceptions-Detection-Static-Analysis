import python

from Variable v
where count(v.getAUse()) < 2
    and exists(
        Assign a |
        a.getTarget(_).(Name).getId() = v.getId()
        and a.getLocation().getFile() = v.getAUse().getLocation().getFile()
    )
select v.getId(), v.getAUse().getLocation().getFile().getShortName()