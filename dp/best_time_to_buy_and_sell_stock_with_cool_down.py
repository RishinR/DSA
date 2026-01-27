# leetcode 309
def main():
    def solve(index, buying):
        if index >= len(prices):
            return 0

        if dp[index][buying] != -1:
            return dp[index][buying]

        # skip today
        cool_down = solve(index + 1, buying)

        # buy today
        if buying:
            buy = solve(index + 1, not buying) - prices[index]
            dp[index][buying] = max(buy, cool_down)
            return dp[index][buying]

        else:
            # if sell then dont call index + 1
            sell = solve(index + 2, not buying) + prices[index]
            dp[index][buying] = max(sell, cool_down)
            return dp[index][buying]

    prices = [1, 2, 3, 0, 2]
    dp = [[-1 for _ in range(2)] for _ in range(len(prices) + 1)]
    result = solve(0, True)
    print(result)


if __name__ == "__main__":
    main()
