def fibonacci(n):
    if n <= 0:
        return None

    if n == 1:
        return 0
    if n == 2:
        return 1
    a = 0
    b = 1
    for x in range (3,n+1) :
        sum = a+b
        a = b
        b = sum
    return (sum)
