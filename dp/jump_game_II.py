def main():
    def solve(index):
        if index >= len(nums) - 1:
            return 0

        if nums[index] == 0:
            return float("inf")

        if index in dp:
            return dp[index]

        ans = float("inf")
        for i in range(1, nums[index] + 1):
            ans = min(ans, 1 + solve(index + i))
        dp[index] = ans
        return dp[index]

    nums = [2, 3, 1, 1, 4]
    dp = {}
    result = solve(0)
    print(result)


if __name__ == "__main__":
    main()
