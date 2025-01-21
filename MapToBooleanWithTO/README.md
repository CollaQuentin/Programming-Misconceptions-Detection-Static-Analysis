# MapToBooleanWithTernaryOperator

## Description

Students tend to use a ternary operator to cast a conditino into a boolean, which is not necessary.

## Symptoms

We're looking for ternary operators which results are `True` and `False`.

## Theorical examples

```py
x = 5
is_greater_than_10 = True if x < 10 else False
```

```py
def is_smaller_than_5(x):
    return True if x < 5 else False
```

## Source
[Progmiscon](https://progmiscon.org/misconceptions/Python/MapToBooleanWithTernaryOperator/)