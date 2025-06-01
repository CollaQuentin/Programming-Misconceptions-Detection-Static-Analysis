def rho(a,b,c):
    p = (b**2)-(4*a*c)
    return p
def n_solutions(a,b,c):
    rho(a,b,c)
    p = (b**2)-(4*a*c)
    if p > 0:
        return 2
    if p==0:
        return 1
    if p < 0:
        return 0
def solution(a,b,c):
    rho(a,b,c)
    n_solutions(a,b,c)
    p = (b**2)-(4*a*c)
    if n_solutions(a,b,c)==1:
        return (-b)/(2*a)
    if n_solutions(a,b,c)==2:
        return (-b-(racine_carree(p)))/(2*a)
    if n_solutions(a,b,c)==0:
        return None
