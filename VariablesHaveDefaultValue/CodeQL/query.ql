import python

from Variable v
where
    v.getId() != "__name__" and v.getId() != "__package__" and
    not exists(BuiltinCallable builtin | builtin.getName() = v.getId()) and
    not exists(Name n | v.getAStore() = n) and
    not exists(Name n | n.getVariable() = v and n.pointsTo().isBuiltin())
select v, v.getScope().getLocation().getFile().getShortName()
