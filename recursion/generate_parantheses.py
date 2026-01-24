def solve(index, n, subarr, result, open, close, balance):
    if index == 2 * n:
        result.append(subarr)
        return

    if open > 0:
        solve(index + 1, n, subarr + "(", result, open - 1, close, balance + 1)

    if close > 0 and balance > 0:
        solve(index + 1, n, subarr + ")", result, open, close - 1, balance - 1)


def main():
    n = 2
    result = []
    solve(0, n, "", result, n, n, 0)
    print(result)


if __name__ == "__main__":
    main()
