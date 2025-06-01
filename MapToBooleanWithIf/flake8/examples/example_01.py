i=2
while i<n:
    if n%i==0:
        is_prime=True
    else:
        is_prime=False
    i+=1
print("prime?"+str(is_prime))
