# leetcode 91


def main():
    s = "226"

    def isvalid(substr):
        if substr[0] == "0":
            return False

        num = int(substr)
        if num >= 1 and num <= 26:
            return True

        return False

    def solve(index, dp):
        if index == len(s):
            return 1

        take_one, take_two = 0, 0
        if isvalid(s[index]):
            take_one = solve(index + 1, dp)
        if index + 1 < len(s) and isvalid(s[index : index + 2]):
            take_two = solve(index + 2, dp)

        return take_one + take_two

    dp = [-1 for _ in range(len(s))]
    result = solve(0, dp)
    print(result)


if __name__ == "__main__":
    main()
