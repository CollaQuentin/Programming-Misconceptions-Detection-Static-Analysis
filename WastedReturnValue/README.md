# WastedReturnValue

## Description

Students sometimes ignore the return value of a function, either because this function didn't need to return anything or simply because they forgot to store it.

## Symptoms

We're looking fucntion calls where the return value of the call is not stored or used (and where the function actually returns something).

## Theorical examples

```py
def foo(bar):
    return -bar

foo(5)
```

## Source
Sorva #38 (Hristova et al., 2003) : *"A `return` value does not need to be stored (even if one needs it later)."*