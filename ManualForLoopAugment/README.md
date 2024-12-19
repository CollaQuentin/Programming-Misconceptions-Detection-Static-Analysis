# ManualForLoopAugment

## Description

Students believe that the control variable of a `for` loop must be manually updated within the loop's body.

## Symptoms

We're looking for increment/decrement of the loop control variable within its body.

## Theorical examples

```py
for i in range(10):
    print(i)
    i += 1
```

```py
for i in range(0, 10, -1):
    i = i - 1
    print(i)
```


## Source
Kim Mens (UCLouvain)