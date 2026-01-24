# leetcode 39
def main():
    def solve(index, subarr, curr_sum):
        if index == len(nums):
            if target == curr_sum:
                result.append(subarr.copy())
            return

        if curr_sum > target:
            return

        subarr.append(nums[index])
        solve(index, subarr, curr_sum + nums[index])

        subarr.pop()
        solve(index + 1, subarr, curr_sum)

    nums = [2, 3, 6, 7]
    target = 7
    result = []
    solve(0, [], 0)
    print(result)


if __name__ == "__main__":
    main()
