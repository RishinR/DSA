# leetcode 322
def main():
    coins = [1, 2, 5]
    amount = 11

    def solve(target):
        if target == 0:
            return 0
        if target < 0:
            return float("inf")

        output = []
        for coin in coins:
            output.append(1 + solve(target - coin))
        return min(output) if output else -1

    if amount == 0:
        return 0

    result = solve(amount)
    if result == float("inf"):
        print(-1)
    else:
        print(result)


if __name__ == "__main__":
    main()
