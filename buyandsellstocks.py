if __name__ == "__main__":
    l = [7,1,5,3,6,4]
    n = len(l)
    c = []
    currmin = 0
    for i in range(0, n):
        if l[currmin] > l[i]:
            currmin = i
        c.append(l[i] - l[currmin])
    print(max(c))