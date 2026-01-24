def solve(n, k):
    if n == 1:
        return 1
    return (solve(n - 1, k) + k - 1) % n + 1


def main():
    n = 40
    k = 7
    output = solve(n, k)
    print(output)


if __name__ == "__main__":
    main()
