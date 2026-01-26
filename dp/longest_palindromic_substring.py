# leetcode 5
def main():
    s = "babad"
    result = ""
    max_len = float("-inf")

    def odd_palindrome(index):
        nonlocal result, max_len
        left, right = index, index
        while left >= 0 and right < len(s):
            if s[left] != s[right]:
                return
            curr_len = right - left + 1
            if curr_len > max_len:
                max_len = curr_len
                result = s[left:right + 1]
            left -= 1
            right += 1

    def even_palindrome(index):
        nonlocal result, max_len
        left, right = index, index + 1
        while left >= 0 and right < len(s):
            if s[left] != s[right]:
                return
            curr_len = right - left + 1
            if curr_len > max_len:
                max_len = curr_len
                result = s[left:right + 1]
            left -= 1
            right += 1

    for i in range(len(s)):
        odd_palindrome(i)
        even_palindrome(i)
    print(result)

if __name__ == "__main__":
    main()