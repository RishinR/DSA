# leetcode 115
def main():
    def solve(i, j):
        if j == len(t):
            return 1
        if i == len(s):
            return 0

        if (i, j) in dp:
            return dp[(i, j)]

        count = solve(i + 1, j)
        if s[i] == t[j]:
            count += solve(i + 1, j + 1)
        dp[(i, j)] = count
        return dp[(i, j)]

    s = "rabbbit"
    t = "rabbit"
    dp = {}
    result = solve(0, 0)
    print(result)


if __name__ == "__main__":
    main()
