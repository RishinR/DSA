nums = [0,0,1,1,1,2,2,3,3,4]
# output = 4, [1, 2, 3, 4]
l = {}
for i in nums:
    l[i] = str(i)
index = 0
for i in l:
    nums[index] = i
    index += 1
for i in range(0, index):
    print(nums[i])
# return index
print(index)
print(l)