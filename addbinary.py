if __name__ == "__main__":
    n1 = input()
    n2 = input()
    a = []
    b = []
    c = []
    # check if they are of the same length or make them so
    if len(n1) != len(n2):
        if len(n1) > len(n2):
            diff = len(n1) - len(n2)
            for i in range(0, diff):
                n2 = "0"+n2
        else:
            diff = len(n2) - len(n1)
            for i in range(0, diff):
                n1 = "0"+n1
    else:
        for i in range(0, len(n1)):
            a.append(int(n1[i]))
        for i in range(0, len(n2)):
            b.append(int(n2[i]))
        for i in range(0, len(n1)):
            c.append(0)
        carry = 0
        #  additon part
        i = len(n1) - 1
        while i > -1:
            if a[i] == 0 and b[i] == 0:
                if carry == 1:
                    c[i] = carry
                    carry = 0
                else:
                    c[i] = 0
            elif a[i] == 0 and b[i] == 1:
                if carry == 1:
                    c[i] = 0
                    carry = 1
                else:
                    c[i] = 1
            elif a[i] == 1 and b[i] == 0:
                if carry == 1:
                    c[i] = 0
                    carry = 1
                else:
                    c[i] = 1
            elif(a[i] == 1 and b[i] == 1):
                if carry == 1:
                    c[i] = 1
                    carry = 1
                else:
                    c[i] = 0
                    carry = 1
            i -= 1
        if (carry == 1):
            c.insert(carry, 1)
    print(c)