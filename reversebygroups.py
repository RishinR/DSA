a = [1, 2, 3, 4, 5, 6, 7, 8]
k = 3
z = len(a)//k
print(z)
i = 0
j = k
count = 0
while True:
    if count == z:
        break
    else:
        print(a)
        s = a[i:j]
        print("s is ", s)
        print(s[::-1])
        a[i:j] = s[::-1]
        print(a)
        i += k
        j += k
        count += 1
print(i)
s = a[i:len(a)]
a[i:len(a)] = s[::-1]
print(a)
