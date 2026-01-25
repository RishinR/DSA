# leetcode 131
def main():
    def ispalindrome(left, right):
        while left < right:
            if s[left] != s[right]:
                return False
            left += 1
            right -= 1
        return True

    def solve(start):
        if start == len(s):
            result.append(path[:])
            return
        for end in range(start, len(s)):
            if ispalindrome(start, end):
                path.append(s[start : end + 1])
                solve(end + 1)
                path.pop()

    s = "aab"
    result = []
    path = []
    solve(0)
    print(result)


if __name__ == "__main__":
    main()
