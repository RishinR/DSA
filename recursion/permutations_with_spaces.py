def solve(index, arr, subarr, result):
    if index == len(arr) - 1:
        result.append(subarr + arr[-1])
        return
    subarr += arr[index]
    solve(index + 1, arr, subarr, result)
    subarr += "_"
    solve(index + 1, arr, subarr, result)


def main():
    s = "abc"
    result = []
    solve(0, s, "", result)
    print(result)


if __name__ == "__main__":
    main()
