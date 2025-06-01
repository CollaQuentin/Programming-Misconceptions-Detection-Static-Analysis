def fibonacci(n):
    pastlast = 0
    last = 1
    if(n>=1):
        print(0)
    if(n>=2):
        print(1)
    if(n>=3):
        for i in range(n-2):
            next = last + pastlast
            return(next)
            pastlast = last
            last = next
