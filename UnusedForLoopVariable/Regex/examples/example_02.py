import math
def fibonacci(n):
    a=0
    b=1
    for i in range((n+2)//2):
        a+=b
        b+=a
    if n%2==1:
        return a
    else:
        return b
