def insertionsort(a):
    for i in range(1, len(a)):
        current = a[i]
        j = i-1
        while (j >= 0 and a[j] > current):
            a[j + 1] = a[j]
            j -= 1
        a[j+1] = current
    return a


if __name__ == "__main__":
    string = input()
    nums = list(map(int, string.split(" ")))
    nums = insertionsort(nums)
    print(nums)
