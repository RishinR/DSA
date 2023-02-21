strs = ["flower","flow","flight"]
minimum = len(strs[0])
for i in range(1, len(strs)):
    if len(strs[i]) < minimum:
        minimum = len(strs[i])
# print(minimum)
flag = True
answer = ""
for i in range (0, minimum):
    out = strs[0][i]
    for j in range(0, len(strs)):
        if out != strs[j][i]:
            flag = False
            break
    if flag and len(strs[0]) > 0:
        answer += out
    else:
        break
print(answer)