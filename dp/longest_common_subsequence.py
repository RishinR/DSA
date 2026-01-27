def main():
    def solve(i, j):
        if i == len(text1) or j == len(text2):
            return 0

        if dp[i][j] != -1:
            return dp[i][j]

        if text1[i] == text2[j]:
            dp[i][j] = 1 + solve(i + 1, j + 1)
            return dp[i][j]
        else:
            dp[i][j] = max(solve(i + 1, j), solve(i, j + 1))
            return dp[i][j]

    text1 = "ABCDGH"
    text2 = "AEDFHR"
    dp = [[-1 for _ in range(len(text2))] for _ in range(len(text1))]
    result = solve(0, 0)
    print(result)


if __name__ == "__main__":
    main()
