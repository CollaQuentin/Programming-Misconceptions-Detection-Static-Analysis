# MapToBooleanWithIf

## Description
Students tend to use an `if-else` statement to cast a condition into a boolean, which is not necessary.

## Symptoms
We're looking for `if-else` statements which do only one thing : assign a value to `True`/`False` or return `True`/`False` depending on the result of the condition.

## Theorical examples

```py
x = 5
if x < 10:
    is_greater_than_10 = True
else:
    is_greater_than_10 = False
```

```py
def is_smaller_than_5(x):
    if bar < 5:
        return True
    else:
        return False
```
## Source

[Progmiscon](https://progmiscon.org/misconceptions/Python/MapToBooleanWithIf/)