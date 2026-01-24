# leetcode 17
def main():
    def solve(index, s, substr):
        if index == len(s):
            result.append(substr)
            return

        for val in hashmap[s[index]]:
            solve(index + 1, s, substr + val)

    s = "23"
    hashmap = {
        "2": ["a", "b", "c"],
        "3": ["d", "e", "f"],
        "4": ["g", "h", "i"],
        "5": ["j", "k", "l"],
        "6": ["m", "n", "o"],
        "7": ["p", "q", "r", "s"],
        "8": ["t", "u", "v"],
        "9": ["w", "x", "y", "z"],
    }
    result = []
    solve(0, s, "")
    print(result)


if __name__ == "__main__":
    main()
