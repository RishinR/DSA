if __name__=="__main__":
    string = input()
    nums = list(map(int, string.split(" ")))
    sum  = 0
    for i in range(0, len(nums)):
        current = 0
        for j in range(i, len(nums)):
            current += nums[j]
            sum += current
            print(current)
    print("sum of all substrings is {}".format(sum))