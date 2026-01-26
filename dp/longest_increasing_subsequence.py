# leetcode 300
def main():
    def solve(index, prev_index):
        if index == len(nums):
            return 0

        if dp[index][prev_index + 1] != -1:
            return dp[index][prev_index + 1]

        # take
        take = 0
        if prev_index == -1 or nums[index] > nums[prev_index]:
            take = 1 + solve(index + 1, index)

        # not take
        not_take = solve(index + 1, prev_index)

        dp[index][prev_index + 1] = max(take, not_take)
        return dp[index][prev_index + 1]

    nums = [10, 9, 2, 5, 3, 7, 101, 18]
    n = len(nums)
    dp = [[-1 for _ in range(n + 1)] for _ in range(n)]
    result = solve(0, -1)
    print(result)


if __name__ == "__main__":
    main()
