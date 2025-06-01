
def rho(a,b,c):
    return b**2-4*a*c

def n_solutions(a,b,c):
    rho(a,b,c)
    if rho(a,b,c) > 0:
        return 2
    if rho(a,b,c) == 0:
        return 1
    else:
        return 0

def solution(a,b,c):
    import math
    if n_solutions(a,b,c) == 1:
        return (-b)/2*a
    elif n_solutions(a,b,c) ==0:
        if ((-b) + math.sqrt(rho(a,b,c))/2*a) > ((-b) - math.sqrt(rho(a,b,c))/2*a):
            return ((-b) - math.sqrt(rho(a,b,c)))/2*a
        else :
            return ((-b) + math.sqrt(rho(a,b,c)))/2*a
