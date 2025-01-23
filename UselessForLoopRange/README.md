# UselessForLoopRange

## Description

Students believe that the only way to iterate over a list is to iterate over the index of the list using `range`.

## Symptoms

We're looking for `for` loops where the index are never used to modify an element of the list.

## Theorical examples

```py
l = [1,2,3,4,5]
for i in range(len(l)):
    print(l[i])
```

## Source
(Inspired from) Sorva #32 (du Boulay, 1986) : *"Difficulty in understanding automated changes to `for` control variables."*