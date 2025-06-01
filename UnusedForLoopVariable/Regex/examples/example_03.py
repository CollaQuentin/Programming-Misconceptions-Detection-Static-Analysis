def fibonacci(n):
    s0=0
    s1=1
    for i in range(n-1):
        s0,s1,s = s1, s0+s1, s0+s1
    return s
