list1 = [1, 5, 7, 9]
list2 = [0, 2, 4, 5, 6, 7]
list3 = []
# output = [1,1,2,3,4,4]
x = 0
y = 0

while x != len(list1) and y !=len(list2):
    if list1[x] < list2[y]:
        list3.append(list1[x])
        x += 1
    elif list1[x] == list2[y]:
        list3.append(list1[x])
        list3.append(list2[y])
        x += 1
        y += 1
    else:
        list3.append(list2[y])
        y+=1

if x != len(list1):
    for i in range(x, len(list1)):
        list3.append(list1[x])
        x += 1
if y != len(list2):
    for i in range(x, len(list2)):
        list3.append(list2[y])
        y += 1

print(list3)