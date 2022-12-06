if __name__=="__main__":
    string = input()
    a = list(map(int, string.split(" ")))
    max = 0
    for i in range(0, len(a)):
        if a[i] > a[max]:
            max = i
        print("max till {} is {}".format(i, a[max]))