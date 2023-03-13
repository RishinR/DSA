a = [1, 2, 3, 2, 3]
out = []
for i in range(0, len(a)):
    if a[i] in a[0:i] and a[i] not in out:
        out.append(a[i])
if len(out) == 0:
    print([-1])
else:
    out.sort()
    print(out)

