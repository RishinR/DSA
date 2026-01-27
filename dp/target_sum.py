# leetcode 494
def main():
    def solve(index, curr_sum):
        if index == len(nums):
            if target == curr_sum:
                return 1
            return 0

        if (index, curr_sum) in dp:
            return dp[(index, curr_sum)]

        dp[(index, curr_sum)] = solve(index + 1, curr_sum + nums[index]) + solve(
            index + 1, curr_sum - nums[index]
        )
        return dp[(index, curr_sum)]

    nums = [1, 1, 1, 1, 1]
    target = 3
    dp = {}
    result = solve(0, 0)
    print(result)


if __name__ == "__main__":
    main()
