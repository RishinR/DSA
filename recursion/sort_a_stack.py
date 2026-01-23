def insert_back(stack, item):
    if not stack or item >= stack[-1]:
        stack.append(item)
        return
    top = stack.pop()
    insert_back(stack, item)
    stack.append(top)


def solve(stack):
    if not stack:
        return
    top = stack.pop()
    solve(stack)
    insert_back(stack, top)


def main():
    stack = [5, 1, 0, 2]
    solve(stack)
    print(stack)


if __name__ == "__main__":
    main()
