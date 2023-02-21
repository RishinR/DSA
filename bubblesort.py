def bubblesort(a):
    for i in range(0, len(a)):
        for j in range(i+1, len(a)):
            if a[i] > a[j]:
                (a[i], a[j]) = (a[j], a[i])
    return a
if __name__=="__main__":
    string = input()
    nums = list(map(int, string.split(" ")))
    nums = bubblesort(nums)
    print(nums)