# MultipleValuesReturn

## Description

Students believe that a single return statement can return multiple values at once. They don't understand that, in reality, it may return ONE tuple containing multiple values.

## Symptoms

We're looking for return statements returning multiple values that are not enclosed by parentheses.

## Theorical examples

```py
def foo(bar):
    return bar, -bar
```

## Source

[Progmiscon](https://progmiscon.org/misconceptions/Python/MultipleValuesReturn/)