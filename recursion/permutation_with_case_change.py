def solve(index, arr, subarr, result):
    if index == len(arr):
        result.append(subarr)
        return
    if arr[index].isalpha():
        solve(index + 1, arr, subarr + arr[index].lower(), result)
        solve(index + 1, arr, subarr + arr[index].upper(), result)
    else:
        solve(index + 1, arr, subarr + arr[index], result)


def main():
    s = "abc"
    result = []
    solve(0, s, "", result)
    print(result)


if __name__ == "__main__":
    main()
