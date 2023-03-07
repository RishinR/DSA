n = 6
l = []
top = 0
if n == 1:
    print([[1]])
    # return [[1]]
else:
    l.append([1])
    for i in range(1, n):
        s = []
        prev = 0
        final = 0
        for j in l[top]:
            num = prev + j
            s.append(num)
            prev = j
        s.append((j+final))
        top += 1
        l.append(s)
    print(l)
    # return l