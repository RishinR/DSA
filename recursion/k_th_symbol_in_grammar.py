def solve(n, k):
    if n == 1 and k == 1:
        return 0
    mid = 2 ** (n - 2)
    if k <= mid:
        return solve(n - 1, k)
    return int(not solve(n - 1, k - mid))


def main():
    n, k = 3, 3
    output = solve(n, k)
    print(output)


if __name__ == "__main__":
    main()
