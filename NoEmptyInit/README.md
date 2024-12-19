# NoEmptyInit

## Description

Students believe that :
- All classes must have an `__init__` method
(and/or)
- All `__init__` methods must do something

## Symptoms
Students will always feel obliged to write an `__init__` method, even if it does not do anything useful. We're looking for `__init__` methods meeting two conditions : 
1. Only contains one statement
2. The statement is either `pass`, `...` or `return` (also triggering the `InitShoudlReturn` misconception)

## Theorical examples

```py
class Dog:
    def __init__(self):
        pass
    
    def bark(self):
        print("Bark !")
```

```py
class Dog:
    def __init__(self):
        ...
    
    def bark(self):
        print("Bark !")
```

```py
class Dog:
    def __init__(self):
        return
    
    def bark(self):
        print("Bark !")
```

## Source

[Progmiscon](https://progmiscon.org/misconceptions/Python/NoEmptyInit/)