# leetcode 97
def main():
    def solve(i, j):
        if i == len(s1) and j == len(s2):
            return True

        if (i, j) in dp:
            return dp[(i, j)]

        k = i + j
        ans = False

        if i < len(s1) and s1[i] == s3[k]:
            ans = solve(i + 1, j)
        if not ans and j < len(s2) and s2[j] == s3[k]:
            ans = solve(i, j + 1)

        dp[(i, j)] = ans
        return dp[(i, j)]

    s1 = "aabcc"
    s2 = "dbbca"
    s3 = "aadbbcbcac"

    if len(s1) + len(s2) != len(s3):
        return False

    dp = {}
    result = solve(0, 0)
    print(result)


if __name__ == "__main__":
    main()
