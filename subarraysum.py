a = [1,2,3,4,5,6,7,8,9,10]
n = len(a)
j = 0
i = 0
s = 10
sum = 0
out = []
while j <= n:
    print(a[i])
    print(a[j])
    if sum == s:
        print("h3")
        out.append(i+1)
        out.append(j)
        break
    elif sum < s:
        print("h2")
        sum += a[j]
        j += 1
    else:
        print("h1")
        sum -= a[i]
        i += 1
    print("sum is ", sum)
if sum == s:
    print(out)
else:
    while i < n:
        sum -= a[i]
        i += 1
    if sum == s:
        print(out)
    else:
        print(-1)
