
def fibonacci(n):
    if n == 0 :
        return(0)
    elif n == 1:
        return(1)
    elif n >= 2:
        fibo0 = 0
        fibo1 = 1
        fibon = 0
        i = 0
        for i in range(2,n+1):
            fibon = fibo0 + fibo1
            fibo0 = fibo1
            fibo1 = fibon
            i += 1
    return(fibon)
