import sys
if __name__=="__main__":
    string = input()
    a = list(map(int, string.split(" ")))
    x = 10**6+2
    index = []
    for i in range(0, x):
        index.append(-1)
    minindex = sys.maxsize
    for i in range(0, len(a)):
        if index[a[i]] != -1:
            minindex = min(minindex, index[a[i]])
        else:
            index[a[i]] = i
    if minindex == sys.maxsize:
        print(-1)
    else:
        print(minindex)
        print(a[minindex])