n = int(input())
y = n
nums = []
sum = 0
while(n > 0):
    rem = n%10
    nums.append(rem)
    n = int(n/10)
print(nums)
for i in nums:
    sum += i**3
print(sum)
if sum == y:
    print("%d is an armstrong number"%y)
else:
    print("%d is not an armstrong number"%y)
