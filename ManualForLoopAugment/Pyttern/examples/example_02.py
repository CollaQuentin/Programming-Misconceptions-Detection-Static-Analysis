
def fibonacci(n):
    fibo = 0
    for i in range(n):
        fibo += i
        i = fibo
    return fibo
