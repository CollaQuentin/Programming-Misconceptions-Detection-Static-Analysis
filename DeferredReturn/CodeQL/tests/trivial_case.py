def foo(bar):
    print("This is before")
    if bar > 5:
        print("This is in the condition")
        return bar
    print("This is after the condition")
    return bar
