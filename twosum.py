hashmap = {}
nums = [2,7,11,15]
out = []
target = 9
# inserting into hashmap
for i in range(0, len(nums)):
    hashmap[nums[i]] = i;
# check if the value in hashmap is present in hashmap
for i in range(0, len(nums)):
    if hashmap.get(target - nums[i]):
        index = hashmap.get(target - nums[i])
        if index != i:    
            out.append(i)
            out.append(index)
            break
print(out)
# print(hashmap)