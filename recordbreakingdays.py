if __name__=="__main__":
    string = input()
    a = list(map(int, string.split(" ")))
    rbdays = 0 # record breaking days
    max = -1
    for i in range(0, len(a)):
        if len(a) == 1:
            rbdays = 1
            break
        elif a[i] > max:
            if a[i] == a[len(a)-1]:    
                max = a[i]
                # print(a[i])
                rbdays += 1
            elif a[i] > a[i+1]:
                max = a[i]
                rbdays += 1
    print(rbdays)        