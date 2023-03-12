def binarysearch(a, left, right, key):
    if left > right:
        return -1
    mid = (left+right)//2
    if a[mid] == key:
        return mid
    elif key < a[mid]:
        return binarysearch(a, left, mid - 1, key)
    else:
        return binarysearch(a, mid + 1, right, key)


if __name__ == "__main__":
    a = [1, 2, 3, 4, 5, 6, 7]
    k = 3
    left = 0
    right = len(a)-1
    x = binarysearch(a, left, right, k)
    print(x)
