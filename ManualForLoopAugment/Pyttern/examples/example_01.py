
def fibonacci(n):
    if n == 0 :
        return(0)
    elif n == 1:
        return(1)
    elif n >= 2:
        suite = 0
        i = 0
        for i in range(2,n+1):
            suite *= n-1 + n-2
            i += 1
        return(suite)

