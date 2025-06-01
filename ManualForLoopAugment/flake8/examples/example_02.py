
def fibonacci(n):
    L=[]
    for i in range(n+1):
        if i == 0:
            L.append(0)
        elif i == 1:
            L.append(1)
        else:
            L.append(L[i-1]+L[i-2])
            i=i-1+i-2
    return (L)
