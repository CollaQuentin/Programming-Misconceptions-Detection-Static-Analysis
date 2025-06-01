r=0
for i in range (2,n//2):
    if n%i==0:
        r=r+1
if (r==0):
    is_prime=True
else:
    is_prime=False
print(is_prime)
