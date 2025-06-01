rep = True

# Boucle de calcul de la suite de Syracuse
while rep == True:
    print(s0)  # Affichage de la valeur courante de s0
    if s0 % 2 == 0:
        s0 = s0 / 2
    else:
        s0 = (3 * s0) + 1
    if s0 == 1:  # Vérification si s0 est égal à 1 pour arrêter la boucle
        rep = False
