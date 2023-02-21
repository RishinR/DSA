def minimum(left, right, a):
    min = left # index of the minimum element
    for i in range(left, right+1):
        if a[i] < a[min]:
            min = i
    return min

if __name__ == "__main__":
    string = input()
    a = list(map(int, string.split(" ")))
    n = len(a)
    for i in range(0, n-1):
        min = minimum(i, n-1, a)
        # swap the intial term with thee minimum term
        tmp = a[i]
        a[i] = a[min]
        a[min] = tmp
    print(a)
        