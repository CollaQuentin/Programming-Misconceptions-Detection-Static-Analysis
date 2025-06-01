def rho(a,b,c):
    return (b**2)-(4*a*c)

def n_solutions(a,b,c):
    if rho(a,b,c) == 0:
        return 1
    elif rho(a,b,c) > 0:
        return 2
    else:
        return 0

def solution(a,b,c):
    if rho(a,b,c) == 0:
        return -b/(2*a)

    elif rho(a,b,c):
        x = (-b+racine_carree(rho(a,b,c)))/2*a
        y = (-b-racine_carree(rho(a,b,c)))/2*a
        if x<y:
            return x
        else:
            return y