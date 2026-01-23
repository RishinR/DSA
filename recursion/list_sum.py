def get_sum(nums, n):
    if n == 0:
        return 0
    return nums[n - 1] + get_sum(nums, n - 1)


def main():
    nums = [1, 2, 3, 4, 5]
    result = get_sum(nums, len(nums))
    print(result)


if __name__ == "__main__":
    main()
