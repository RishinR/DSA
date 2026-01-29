def main():
    index = 3
    result = [[1]]

    for i in range(index):
        curr = result[-1]
        output = []
        for j in range(len(curr) + 1):
            if j == 0:
                output.append(curr[0])
            elif j == len(curr):
                output.append(curr[len(curr) - 1])
            else:
                output.append(curr[j - 1] + curr[j])
        result.append(output)
    print(result[index])


if __name__ == "__main__":
    main()
