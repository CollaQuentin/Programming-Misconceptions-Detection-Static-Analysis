# SelfAssignable

## Description

Students believe that it can be useful/necessary to assign values to the `self` variable in a class.

## Symptoms

We're looking for assignemnts to a variable named `self` in a class.

## Theorical examples

```py
class Dog:
    def __init__(self, name):
        self = Dog(name)
```

## Source
[Progmiscon](https://progmiscon.org/misconceptions/Java/ThisAssignable/)