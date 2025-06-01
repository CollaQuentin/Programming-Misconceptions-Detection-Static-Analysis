
import math as m
def rho(a,b,c):
    p = (b**2)-4*a*c
    return p
rho(a,b,c)

def n_solutions(a,b,c):
    if rho(a,b,c) > 0:
        return 2
    elif rho(a,b,c) == 0:
        return 1
    else:
        return 0
n_solutions(a,b,c)

def solution(a,b,c):
    if n_solutions(a,b,c) == 1:
        result = (-b + m.sqrt(rho(a,b,c)))/2*a
        return result
    if n_solutions(a,b,c) == 2:
        result = (-b - m.sqrt(rho(a,b,c)))/2*a
        if result > (-b + m.sqrt(rho(a,b,c)))/2*a:
            return (-b + m.sqrt(rho(a,b,c)))/2*a
        else:
            return result
    else:
        return False


