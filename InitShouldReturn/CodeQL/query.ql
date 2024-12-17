import python

from Function f, Return r
where f.isMethod() 
    and f.getName() = "__init__"
    and f.getBody().contains(r)
select f, "The __init__ method has a return statement.", f.getLocation().getFile().getShortName()
