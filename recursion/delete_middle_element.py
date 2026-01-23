def delete_middle(stack, k):
    if k == 0:
        stack.pop()
        return
    temp = stack.pop()
    delete_middle(stack, k - 1)
    stack.append(temp)


def solve(stack):
    n = len(stack)
    if n == 0:
        return []
    delete_middle(stack, n // 2)


def main():
    stack = [1, 2, 3, 4, 5, 6]
    solve(stack)
    print(stack)


if __name__ == "__main__":
    main()
