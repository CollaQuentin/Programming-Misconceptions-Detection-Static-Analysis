def fact(n):
    if n >= 1:
        facto = 1
        for i in range (1,n+1):
            facto = facto*i
        return (facto)
    elif n == 0:
        return (1)
