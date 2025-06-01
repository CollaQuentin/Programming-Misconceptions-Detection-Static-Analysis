def fact(n):
    if n==0:
        facto = 1
        return (facto)
    else:
        facto=n
        for i in range (1,n):
            facto= facto*(n-i)
        return (facto)
