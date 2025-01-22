# VariablesHaveDefaultValue

## Description

Students believe that they can use a variable without defining it first, as if undefined variables had a default value.

## Symptoms

We're looking for any use of a variable that is not defined.

## Theorical examples

```py
print(x)
# where x is not defined
```

```py
a += 1
# where a is no defined
```

## Discussion

The logic behind this implementation is not necessarily the best. In fact, it is frequent for beginners to forget to assign a value to a variable before trying to use it (in an accumulator pattern, for example). This does not mean that they thought the variable would receive a default value (as the misconception defines).

## Source
Sorva #10 (du Boulay, 1986; Samurçay, 1989) : *"Variables always receive a particular default value upon creation."*