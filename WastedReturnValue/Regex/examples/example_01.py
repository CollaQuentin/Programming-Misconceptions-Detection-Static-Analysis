def rho(a,b,c):
    rho = (b**2)-(4*a*c)
    return rho

def n_solutions(a,b,c):
    rho = rho(a,b,c)
    if rho > 0:
        return 2
    elif rho == 0:
        return 1
    else:
        return 0

def solution(a,b,c):
    rho = rho(a,b,c)
    nombre = n_solutions(a,b,c)
    if nombre == 1:
        sol = (b*(-1))/(2*a)
        return sol
    elif nombre == 2:
        sol_1 = (b*(-1)-racine_carree(rho))/(2*a)
        sol_2 = (b*(-1)+racine_carree(rho))/(2*a)
        if sol_1 <= sol_2:
            return sol_1
        else:
            return sol_2
def second_degré(a,b,c):
    nbr = n_solutions(a,b,c)
    if nbr != 0:
        solution(a,b,c)
