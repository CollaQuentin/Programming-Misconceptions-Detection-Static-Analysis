# NewAttributesInMethod

## Description

Students believe that it is a good practice to create new attributes for a class in a method (that is not the `__init__` method).

## Symptoms

We're looking for a definition of a new attribute in a method that is not the `__init__` method.

## Theorical examples

```py
class Dog:
    def __init__(self, name):
        self.name = name

    def give_birth(self, puppy_name):
        self.puppy = Dog(puppy_name)
```

## Source
(Inspired from) Sorva #117 (Ragonis and Ben-Ari, 2005) : *""You can define a (Java) method that adds an attribute to the class.""*