# leetcode 139
def main():
    s = "leetcode"
    wordDict = ["leet", "code"]

    def solve(index, dp):
        if index == len(s):
            return True
        
        if dp[index] != -1:
            return dp[index]

        for word in wordDict:
            if index + len(word) <= len(s) and s[index: index + len(word)] == word:
                if solve(index + len(word), dp):
                    dp[index] = True
                    return dp[index]
                
        dp[index] = False
        return dp[index]

    dp = [-1 for _ in range(len(s) + 1)]
    result = solve(0, dp)
    print(result)

if __name__ == "__main__":
    main()