def fibonacci(n):
    a=0
    b=1
    if n==0:
        return 0
    elif n==1:
        return 1
    else:
        while n>=2:
            return a+b
            a=b
            b=a+b
