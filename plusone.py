digits = [1,2,3]
number = ""
final = []
for i in digits:
    number += str(i)
val = int(number)
val += 1
out = str(val)
index = 0
for i in out:
    final.append(int(i))
# return final
print(final)