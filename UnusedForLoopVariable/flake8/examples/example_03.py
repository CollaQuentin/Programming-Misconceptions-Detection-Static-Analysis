def fibonacci(n):        #Fn=Fn−1+Fn−2
    a= 0
    b= 1
    c=0
    for i in range(1,n):
        c=a+b
        a=b
        b=c
    return c
