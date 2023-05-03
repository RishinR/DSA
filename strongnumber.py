from math import factorial
# n = input("Enter a number: ")
for j in range(1000, 10000):
    n = str(j)
    sum = 0
    for i in n:
        sum += factorial(int(i))
    if sum == int(n):
        print("%d is Strong Number", format(sum))
    # else:
        # print("%d Not a Strong Number", format(sum))
