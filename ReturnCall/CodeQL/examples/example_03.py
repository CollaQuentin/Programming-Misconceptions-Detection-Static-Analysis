
def fact(n):
    '''pré: rentrez un nombre > 0
       post: vous renvoie la factorielle de ce nombre'''
    if n==0 or n==1:
        return (1)
    else:
        som = 1
        for i in range(n, 2, -1):
            som *= n
