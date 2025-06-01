
def fibonacci(n):
    elem=[0,1]
    for a in range (2,n+1):
        elem.append(elem[a-2]+elem[a-1])
        a+=1
    return elem[n]
