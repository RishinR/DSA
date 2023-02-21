s = "[]]"
opening = {"(", "[", "{"}
closing = {")", "]", "}"}
stack = []
str = ""
count = 0
flag = False
for i in s:
    if i in opening:
        stack.append(i)
        flag = False
    else:
        if len(stack) != 0:
            str = stack.pop()
            if str == "{" and i == "}" or str == "(" and i == ")" or str == "[" and i == "]":
                flag = True
            else:
                flag = False
                break
        else:
            flag = False
            break
if len(stack) != 0:
    print(False)
else:
    print(flag)