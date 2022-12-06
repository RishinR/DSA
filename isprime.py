import math
def isprime(x):
    prime = True
    for i in range(2, int(math.sqrt(x)+1)):
        if x % i == 0:
            prime = False
            break
    return prime

if __name__ == "__main__":
    n1 = int(input())
    n2 = int(input())
    print("prime numbers int between {} and {} are: ".format(n1, n2))
    for i in range(n1, n2):
        if isprime(i):
            print(i)