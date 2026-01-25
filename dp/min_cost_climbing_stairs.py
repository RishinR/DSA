def main():
    def solve(index, dp):
        if index >= len(cost):
            return 0

        if dp[index] != -1:
            return dp[index]

        one = cost[index] + solve(index + 1, dp)
        two = cost[index] + solve(index + 2, dp)

        dp[index] = min(one, two)
        return dp[index]

    cost = [10, 15, 20]
    dp = [-1 for _ in range(len(cost) + 2)]
    result = min(solve(0, dp), solve(1, dp))
    print(result)


if __name__ == "__main__":
    main()
