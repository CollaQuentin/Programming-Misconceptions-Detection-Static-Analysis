def fact(n):
    """pre : n est un nombre entier strictement positif
    post : retourne la factorielle de n
    """
    factorielle = 1
    for i in range(1,n+1):
        factorielle = factorielle*i
        return (factorielle)
