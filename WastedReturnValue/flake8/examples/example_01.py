def rho(a, b, c):
    r = racine_carree((b ** 2) - (4 * a * c))
    return r

def n_solutions(a, b, c):
    rho(a, b, c)
    if rho(a, b, c) == 0:
        n = 1
    elif rho(a, b, c) > 0:
        n = 2
    else:
        n = 0
    return n


def solution(a, b, c):
    if n_solutions(a, b, c) == 0:
        pass
    elif n_solutions(a, b, c) == 1:
        sol = -b / (2 * a)
    elif n_solutions(a, b, c) == 2:
        sol1 = (racine_carree(rho(a, b, c)) - b) / (2 * a)
        sol2 = ((-b) - racine_carree(rho(a, b, c))) / (2 * a)
        if sol1 <= sol2:
            sol = sol1
        else:
            sol = sol2
    return sol
