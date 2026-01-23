def one_to_n(n):
    if n == 0:
        return
    one_to_n(n - 1)
    print(n, end=" ")


def n_to_one(n):
    if n == 0:
        return
    print(n, end=" ")
    n_to_one(n - 1)


def main():
    n = 5
    print("One to n is: ", end="")
    one_to_n(n)
    print()
    print("N to one is: ", end="")
    n_to_one(n)


if __name__ == "__main__":
    main()
