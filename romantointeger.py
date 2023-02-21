roman = "III"
# print(roman)
number = 0
convert = {"I":1, "V":5, "X":10, "L":50, "C":100, "D":500, "M":1000}
prevvalue = 0
for i in reversed(roman):
    # print(i)
    value = convert[i]
    if prevvalue > value:
        number -= value
    else:
        number += value
    prevvalue = value
print(number)