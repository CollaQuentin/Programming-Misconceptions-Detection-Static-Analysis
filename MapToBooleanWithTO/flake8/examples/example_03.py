for i in range(2, int(n ** 0.5) + 1):
    if n % i == 0:
        is_prime = False
        break
if n == 2 or n == 1:
    is_prime = True if n == 2 else False

print(is_prime)
