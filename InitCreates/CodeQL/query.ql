import python

from Class cls, Function f, Call c
where f.getName() = "__init__"
    and cls.contains(f)
    and f.contains(c)
    and c.getFunc().toString() = cls.getName()
select cls, c.getLocation().getFile().getShortName()
