# leetcode 167
def main():
    numbers = [2, 7, 11, 15]
    target = 9

    left = 0
    right = len(numbers) - 1
    while left < right:
        curr_sum = numbers[left] + numbers[right]
        if curr_sum < target:
            left += 1
        elif curr_sum > target:
            right -= 1
        else:
            print([left + 1, right + 1])
            return
        
if __name__ == "__main__":
    main()