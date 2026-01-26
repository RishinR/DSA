# leetcode 152

def main():
    nums = [2, 3, -2, 4]
    n = len(nums)

    pre, suf = 1, 1
    left, right = [0 for _ in range(n)], [0 for _ in range(n)]

    for i in range(n):
        pre *= nums[i]
        suf *= nums[n - i - 1]
        left[i] = pre
        right[n - i - 1] = suf
        if suf == 0:
            suf = 1
        if pre == 0:
            pre = 1
    
    result = float("-inf")
    for i in range(n):
        result = max(result, left[i], right[i])
    print(result)

if __name__ == "__main__":
    main()