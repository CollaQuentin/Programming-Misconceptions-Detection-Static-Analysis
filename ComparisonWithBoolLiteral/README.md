# ComparisonWithBoolLiteral

## Description

Students believe that *"to test whether an expression is True or False, one must compare it to True or to False"*.

## Symptoms

We're looking for any occurences of comparisons (using `==`) between a value and a boolean litteral (True/False).

## Theorical examples

```py
if CONDITION == True:
    ...
# instead of
if CONDITION:
    ...
```
```py
while CONDITION != False:
    ...
# instead of
while CONDITION:
    ...
```
```py
def is_false(condition):
    return condition == False
    # instead of 
    return not condition
```

## Source
[Progmiscon](https://progmiscon.org/misconceptions/Python/ComparisonWithBoolLiteral/)