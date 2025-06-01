def fibonacci(n):
    n1 = 0
    n2 = 1
    for i in range(2, n):
        suivant = n1 + n2
        n1 = n2
        n2 = suivant
    print(suivant)
