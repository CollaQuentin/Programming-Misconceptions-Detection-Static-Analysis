
nombreDiviseur = 0
for i in range (1,n+1):
    if n % i == 0  :
        nombreDiviseur = nombreDiviseur + 1

if nombreDiviseur == 2 :
    is_prime = True
else :
    is_prime = False
