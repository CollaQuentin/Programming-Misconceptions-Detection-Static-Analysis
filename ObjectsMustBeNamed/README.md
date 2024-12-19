# NoEmptyInit

## Description

Students believe that you can't instantiate an object without storing it in a variable.

## Symptoms

Students might store objects and values in variable only to use them once.

## Theorical examples

```py
a = 1
print(a)
# never uses `a` again
```

**The following example is not considered to be a misconception because the variable is used within a loop :**
```py
big_list = compute_list()
for i in range(100):
    if i in big_list:
        print("Yes")
```

## Source

[Progmiscon](https://progmiscon.org/misconceptions/Python/ObjectsMustBeNamed/)