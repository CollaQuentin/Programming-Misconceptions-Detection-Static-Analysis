# InitCreates

## Description

Students believe that the `__init__` method should create a new object (by initializing it manually in the method).

## Symptoms

We're looking for an object instanciation within its `__init__` method.

## Theorical examples

```py
class Dog:
    def __init__(self, name):
        self.name = name
        self.dog = Dog(name)  #  <- infinite recursion
```

## Source
[Progmiscon](https://progmiscon.org/misconceptions/Python/InitCreates/)