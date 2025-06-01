not_prime = 0
if n > 1:
    for i in range(1, n+1):
        n_is_prime = n % i
        if n_is_prime == 0:
            not_prime += 1
    if not_prime >= 3:
        is_prime = False
    else:
        is_prime = True
else:
    is_prime = False
