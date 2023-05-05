nums = [432,43243]
nums = list(map(str, nums))
for i in range(len(nums)):
    for j in range(i+1, len(nums)):
        if int(nums[i] + nums[j]) > int(nums[j] + nums[i]):
            pass
        else:
            (nums[i], nums[j]) = (nums[j], nums[i])
out = ""
for i in nums:
    out += i
print(out) 
# return out
