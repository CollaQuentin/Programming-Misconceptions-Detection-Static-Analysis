# CannotChainMemberAccesses

## Description

Students believe that it is impossible to chain multiple attribute accesses when interacting with an object.

## Symptoms

We're looking for places where students access an attribute's attribute in two operations instead of one.

## Theorical examples

```py
n = node.next
print(n.value)
# instead of print(node.next.value)
```

## Source
[Progmiscon](https://progmiscon.org/misconceptions/Java/CannotChainMemberAccesses/)