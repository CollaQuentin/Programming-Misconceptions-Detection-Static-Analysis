# NoReservedWords

## Description
Students think that they can name their variables/functions/classes/ anything, but Python reserves [some words](https://docs.python.org/3/reference/lexical_analysis.html#keywords) (`if`, `else`, `with`, ...)

## Symptoms
We're looking for any attempt to use a reserved python keywords as a variable/argument/function/class/...

## Theorical examples

```py
pass = True
for = 3
try = 1
# ...
```
## Source

[Progmiscon](https://progmiscon.org/misconceptions/Python/NoReservedWords/)