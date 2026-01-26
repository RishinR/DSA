# leetcode 647
def main():
    s = "abc"
    result = 0

    def odd_palindrome(index):
        nonlocal result
        left, right = index, index
        while left >= 0 and right < len(s):
            if s[left] != s[right]:
                return
            result += 1
            left -= 1
            right += 1

    def even_palindrome(index):
        nonlocal result
        left, right = index, index + 1
        while left >= 0 and right < len(s):
            if s[left] != s[right]:
                return
            result += 1
            left -= 1
            right += 1

    for i in range(len(s)):
        odd_palindrome(i)
        even_palindrome(i)
        
    print(result)

if __name__ == "__main__":
    main()