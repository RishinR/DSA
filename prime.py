# prime number 
import math
n = int(input())
isprime = True
for i in range(2, int(math.sqrt(n))+1):
    if n % i == 0:
        isprime = False
        print("%d is not a prime number"%n)
        break
if(isprime):
    print("%d is a prime number"%n)
    