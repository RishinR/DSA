# leetcode 416
def main():
    def solve(index, curr_sum, target):
        if curr_sum == target:
            return True
        if curr_sum > target or index == len(nums):
            return False

        if dp[index][curr_sum] != -1:
            return dp[index][curr_sum]

        dp[index][curr_sum] = solve(index + 1, curr_sum + nums[index], target) or solve(
            index + 1, curr_sum, target
        )
        return dp[index][curr_sum]

    nums = [1, 5, 11, 5]
    target = sum(nums)

    if target % 2 != 0:
        print(False)
        return

    target = target // 2
    dp = [[-1 for _ in range(sum(nums) + 1)] for _ in range(len(nums) + 1)]
    result = solve(0, 0, target)
    print(result)


if __name__ == "__main__":
    main()
