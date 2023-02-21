x = 20
preval = 1
flag = False
for i in range(1, int(x/2)+1):
    if i*i > x:
        print(preval)
        flag = True
        break
    elif i*i == x:
        print(i)
        flag = True
        break
    else:
        preval = i
if flag == False:
    print(preval)