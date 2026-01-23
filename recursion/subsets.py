def solve(index, s, substr, result):
    if len(s) == index:
        result.append("".join(substr.copy()))
        return

    # take value in index
    substr.append(s[index])
    solve(index + 1, s, substr, result)

    # not take value in index
    substr.pop()
    solve(index + 1, s, substr, result)


def main():
    s = "abcde"
    subsets = []
    solve(0, s, [], subsets)
    print(subsets)


if __name__ == "__main__":
    main()
