# leetcode 198


def main():
    def solve(index, dp):
        if index >= len(nums):
            return 0

        if dp[index] != -1:
            return dp[index]

        rob_current = nums[index] + solve(index + 2, dp)
        skip_current = solve(index + 1, dp)
        return max(rob_current, skip_current)

    nums = [1, 2, 3, 1]
    dp = [-1 for _ in range(len(nums))]
    result = solve(0, dp)
    print(result)


if __name__ == "__main__":
    main()
