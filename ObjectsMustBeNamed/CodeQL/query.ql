import python

from Variable v
where count(v.getAUse()) < 2
    and exists(
        Assign a |
        a.getTarget(_).(Name).getId() = v.getId()
        and a.getLocation().getFile() = v.getAUse().getLocation().getFile()
    )
select v.getId(), v.getAUse().getLocation().getFile().getShortName()

// predicate notUsedInALoop(Variable v, Assign a) {
//     not exists(
//         For loop |
//         loop.contains(v.getALoad()) and not loop.contains(a)
//     )
//     and not exists(
//         While loop |
//         loop.contains(v.getALoad()) and not loop.contains(a)
//     )
// }
// 
// from Variable v, Assign a
// where count(v.getAUse()) < 2 
//     and a.getTarget(_).(Name).getId() = v.getId()
//     and a.getLocation().getFile() = v.getAStore().getLocation().getFile()
//     // and notUsedInALoop(v, a)
// select v.getId(), count(v.getAUse()), a.getLocation().getFile().getShortName()
