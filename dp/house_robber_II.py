# leetcode 213

def main():
    def solve(index, arr, dp):
        if index >= len(arr):
            return 0
        
        if dp[index] != -1:
            return dp[index]
        
        rob_current = arr[index] + solve(index + 2, arr, dp)
        skip_current = solve(index + 1, arr, dp)
        dp[index] = max(rob_current, skip_current)
        return dp[index]

    nums = [2, 3, 2]

    if len(nums) == 1:
        return nums[0]

    dp1 = [-1 for _ in range(len(nums))]
    dp2 = [-1 for _ in range(len(nums))]
    result = max(solve(0, nums[:-1], dp1), solve(0, nums[1:], dp2))
    print(result)

if __name__ == "__main__":
    main()