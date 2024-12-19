# InitShouldReturn

## Description

Students believe that the `__init__` method from a class should return something (an object instance or anything in most cases).

## Symptoms

We're looking for `return` statements in `__init__` methods

## Theorical examples

```py
class Dog:
    def __init__(self, name):
        self.name = name
        return Dog(name)
```

```py
class Dog:
    def __init__(self, name):
        self.name = name
        return name
```

```py
class Dog:
    def __init__(self, name):
        self.name = name
        return
```

## Source
Inspired from [Progmiscon's InitReturnsObject](https://progmiscon.org/misconceptions/Python/InitReturnsObject/)