# UnusedForLoopVariable

## Description

Students sometimes forget that the point of a `for` loop is to iterate over a structure and to execute a same statements while a control variable updates itself as it iterates through the structure.

## Symptoms

We're looking for `for` loops where the control variable is not used within the body of the loop.

## Theorical examples

```py
for i in range(10):
    print('Hello, World !')
```

```py
for i in range(10):
    i = 0  # The control variable is redefined without being used
    print(i)
```

**We will tolerate the case where the control varaiable is named `_`, such as :**

```py
for _ in range(10):
    print("Hello, World !")
```

## Source

Kim Mens (UCLouvain)