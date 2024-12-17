import python

from ImmutableLiteral bool, Compare comp
where (bool.toString() = "True" or bool.toString() = "False")
    and (
        comp.compares(bool, _, _)
        or comp.compares(_, _, bool)
    )
select comp, comp.getLocation().getFile().getShortName()
