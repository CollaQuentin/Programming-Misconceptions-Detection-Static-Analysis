# ParenthesesOnlyIfArgument

## Description
Students believe that they call a function without using parentheses if the function doesn't have any argument.

## Symptoms
We're looking for students who uses function names without parentheses behind.

## Theorical examples

```py
def foo():
    return "bar"

print(foo)  # expects "bar"
```

## Discussion

It can be useful in some cases to use a function as an object (= without parentheses behind), but it is unlikely required or a good practice to do so as a first grader learning the basics of programming.

## Source

[Progmiscon](https://progmiscon.org/misconceptions/Python/ParenthesesOnlyIfArgument/)