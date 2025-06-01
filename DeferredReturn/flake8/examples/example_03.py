def fibonacci(n):
    f=0
    l=[0,1]
    if n == 1:
        f=1
    return f
    for i in range (n-1):
        f= l[-1] + l[-2]
        l.append(f)
    return f
