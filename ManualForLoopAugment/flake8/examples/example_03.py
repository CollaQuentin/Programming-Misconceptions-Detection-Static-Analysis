
def fibonacci(n):
    n1=0
    n2=1
    if n<=1:
        f=n
    for i in range (2, n):
        s=n1 + n2
        n1=n2
        n2=s
        f=n2+n1
        i+=1
    return (f)
