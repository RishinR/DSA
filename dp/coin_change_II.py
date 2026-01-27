# leetcode 518
def main():
    def solve(index, target):
        if target < 0 or index == len(coins):
            return 0
        if target == 0:
            return 1
        
        if (index, target) in dp:
            return dp[(index, target)]

        dp[(index, target)] = solve(index, target - coins[index]) + solve(index + 1, target)
        return dp[(index, target)]
        
    amount = 5
    coins = [1, 2, 5]
    dp = {}
    result = solve(0, amount)
    print(result)


if __name__ == "__main__":
    main()
