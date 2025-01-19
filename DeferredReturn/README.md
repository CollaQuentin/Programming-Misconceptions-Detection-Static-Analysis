# DeferredReturn

## Description
Students believe that statements after a `return` statement will be executed at some point.

## Symptoms
We're looking for any statement after a `return`.

## Theorical examples

```py
def foo(bar):
    return -bar
    print(f"The opposite of {bar} is {-bar}")
```

## Source

[Progmiscon](https://progmiscon.org/misconceptions/Python/DeferredReturn/)