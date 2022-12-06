n = int(input())
reverse = 0
while(n > 0):
    rem = n%10
    reverse = 10*reverse + rem
    # print(reverse)
    n = int(n/10)
print(reverse)
# reverse = str(n)
# reversed_string = reverse[::-1]
# reversed_num = int(reversed_string)
# print(reversed_num)