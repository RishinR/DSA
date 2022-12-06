import factorial


def ncr(n, r):
    n1 = factorial.factorial(n)
    n2 = factorial.factorial(r)
    n3 = factorial.factorial(n-r)
    result = int(n1/(n2*n3))
    return result


if __name__ == "__main__":
    # n = int(input())
    # r = int(input())
    # print(ncr(n, r))
    # now we will print th e pascal's triangle

    rows = 7
    for i in range(0, rows):
        for j in range(0, i+1):
            print(ncr(i, j), end=" ")
        print("")
