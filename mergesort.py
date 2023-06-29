a = [2, 1, 5, 3, 7, 0, 23, 12]
b = [0]*10


def merge(low, mid, high):
    i = low
    x = low
    y = mid + 1
    while (x <= mid and y <= high):
        if (a[x] < a[y]):
            b[i] = a[x]
            x += 1
        else:
            b[i] = a[y]
            y += 1
        i += 1
    if(x <= mid):
        for k in range(x, mid + 1):
            b[i] = a[k]
            i += 1
    else:
        for k in range(y, high+1):
            b[i] = a[k]
            i += 1
    for k in range(low, high+1):
        a[k] = b[k]

def mergeSort(low, high):
    if (low < high):
        mid = (low + high)//2
        mergeSort(low, mid)
        mergeSort(mid + 1, high)
        merge(low, mid, high)

mergeSort(0, len(a)-1)
print(a)

