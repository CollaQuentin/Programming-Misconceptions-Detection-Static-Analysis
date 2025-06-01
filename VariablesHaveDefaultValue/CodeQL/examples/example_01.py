
def fact(n):
    factorielle = 1
    if n < 0:
        print ("la factorielle d'un négatif n'existe pas")
    elif n == 0:
        print("la factorielle de 0 est 1")
    else:
        for i in range (1,n+1):
            factorielle = factorielle*i
        print ('la factorielle de',n, "est",factorielle)
print()
fact(n)
