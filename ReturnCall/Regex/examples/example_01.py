def fact(n) :
    fact=1
    for k in range(n,1,-1):
        fact = k * fact
    return(fact)
