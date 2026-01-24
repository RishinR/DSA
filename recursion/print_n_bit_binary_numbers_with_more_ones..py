def solve(index, n, substr, one, zero, result):
    if index == n:
        result.append(substr)
        return
    solve(index + 1, n, substr + "1", one + 1, zero, result)
    if zero < one:
        solve(index + 1, n, substr + "0", one, zero, result)


def main():
    n = 3
    result = []
    solve(1, n, "1", 1, 0, result)
    print(result)


if __name__ == "__main__":
    main()
