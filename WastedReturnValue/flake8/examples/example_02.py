def rho(a, b, c):
    return b*b-4*a*c
def n_solutions(a, b, c):
    return 0 if rho(a, b, c) < 0 else (1 if not rho(a, b, c) else 2)
def solution(a, b, c):
    rho(a, b, c)
    s = -b/a
    p = c/a
    return (s/2)-racine_carree((s/2)**2-c)
