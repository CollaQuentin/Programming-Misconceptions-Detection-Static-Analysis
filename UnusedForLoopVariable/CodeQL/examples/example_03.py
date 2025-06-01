def fibonacci(n):
    f0=0
    f1=1
    l=[0,1]
    for i in range (2, n+1):
        fn=f0+f1
        f0=f1
        f1=fn
        l.append(fn)
    return l[n]
