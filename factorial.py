def factorial(x):
    fact = 1
    while(x > 0):
        fact *= x
        x -= 1
    return fact
if __name__ == "__main__":
    n = int(input())
    print(factorial(n))
