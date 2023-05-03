s = "+-42"
y = ""
# sign number remove all white spaces before and after
isdigit = False

for i in s:
    if i == " " and isdigit == False:
        pass
    elif i == "+" and isdigit == False:
        isdigit = True
    elif i == "-" and isdigit == False:
        isdigit = True
        y += "-"
    elif (ord(i)-ord("0")) in range(10):
        isdigit = True
        y += i
    else:
        break
if len(y) == 0:
    print(0)
    # return(0)
elif y == "+" or y == "-":
    # return 0
    print(0)
else:
    z = int(y)
    if z > 2**31 -1:
        # return(2**31 - 1)
        print(2**31 - 1)
    elif z < -2**31:
        # return(-2**31)
        print(-2**31)
    # print(z)
    else:
        # return(z)
        print(z)