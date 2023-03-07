import itertools

def count_permutations(n, a, b, x):
    c = []
    for i in range(n):
        if x[i] == 0:
            c.append(-1)
        elif x[i] == a[i]:
            c.append(a[i])
        else:
            c.append(b[i])
    count = 0
    for perm in itertools.permutations(range(1, n+1)):
        valid_perm = True
        for i in range(n):
            if x[i] == 0:
                continue
            if c[i] != perm[i]:
                valid_perm = False
                break
        if valid_perm:
            count += 1
    return count

if __name__ == "__main__":
    a = [1, 2, 3, 4, 5, 6, 7]
    b = [2, 3, 1, 7, 6, 5, 4]
    x = [2, 0, 1, 0, 0, 0, 0]
    count = count_permutations(7, a, b, x)
    print(int(count/3))