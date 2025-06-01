boucle = True
while(boucle == True):
    print(s0)
    if(s0 == 1):
        boucle = False
    elif(s0/2 == 0):
        s0 = int(s0/2)
    else:
        s0 = int(s0*3+1)
