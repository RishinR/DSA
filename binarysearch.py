def binarysearch(a, x):
    left = 0
    right = len(a) - 1
    while (left <= right):
        mid = int((left + right)/2)
        if (a[mid] == x):
            return mid
        elif (x > a[mid]):
            left = mid + 1
        else:
            right = mid - 1
    return -1


if __name__ == "__main__":
    n = int(input())
    string = input()
    a = list(map(int, string.split(" ")))
    index = binarysearch(a, n)
    if index != -1:
        print("The number {} is found at index {}".format(n, index))
    else:
        print("The element is not present in the list")
