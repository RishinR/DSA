# leetcode 40
def main():
    def solve(index, subarr, curr_sum):
        if index == len(nums):
            if target == curr_sum:
                result.append(subarr.copy())
            return

        if curr_sum > target:
            return

        subarr.append(nums[index])
        solve(index + 1, subarr, curr_sum + nums[index])
        subarr.pop()

        while index + 1 < len(nums) and nums[index] == nums[index + 1]:
            index += 1
        solve(index + 1, subarr, curr_sum)

    nums = [10, 1, 2, 7, 6, 1, 5]
    target = 8
    nums.sort()
    result = []
    solve(0, [], 0)
    print(result)


if __name__ == "__main__":
    main()
