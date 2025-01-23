# IfIsLoop

## Description

Students believe that the body of an `if` statement is executed as long as its condition evaluates to True. In other words, students confuse `if` and `while` statements.

## Symptoms

We're looking for places where a member of the condition of an `if` statement is modified within the body of the same `if` statement. We can guess that the student meant to use the said variable as a control variable for a `while` loop.

## Theorical examples

```py
x = 0
if x < 10:
    x += 1
```

## Source
[Progmiscon](https://progmiscon.org/misconceptions/Python/IfIsLoop/)