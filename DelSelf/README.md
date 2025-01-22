# DelSelf

## Description

Students believe that it is possible to define a method that can destroy the object `self`.

## Symptoms

We're looking for any instance of `del self`.

## Theorical examples

```py
class Bomb:
    def destroy(self):
        del self
```


## Source
Sorva #128 (Ragonis and Ben-Ari, 2005) : *"You can define a method that destroys the object itself."*