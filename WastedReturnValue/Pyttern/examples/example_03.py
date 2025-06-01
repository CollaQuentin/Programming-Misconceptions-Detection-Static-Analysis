
from math import*
#ax²+bx+c=0
def rho(a,b,c):
    rho=(b**2)-(4*a*c)
    return(rho)
def n_solutions(a,b,c):
    if rho(a,b,c)==0:
        return(1)
    elif rho(a,b,c)>0:
        return(2)
    else:
        return(0)
def solution(a,b,c):
    rho(a,b,c)
    if rho(a,b,c)>0:
        sol1=-b+sqrt(rho(a,b,c))/(2*a)
        sol2=-b-sqrt(rho(a,b,c))/(2*a)
        if abs(sol1)<abs(sol2):
            return(sol1)
        else:
            return(sol2)
    elif rho(a,b,c)==0:
        sol=-b/(2*a)
        return(sol)
    else:
        return()


