def main():
    def solve(index, dp):
        if index >= n - 1:
            return 1

        if dp[index] != -1:
            return dp[index]

        dp[index] = solve(index + 1, dp) + solve(index + 2, dp)
        return dp[index]

    n = 2
    dp = [-1 for _ in range(n + 1)]
    result = solve(0, dp)
    print(result)


if __name__ == "__main__":
    main()
