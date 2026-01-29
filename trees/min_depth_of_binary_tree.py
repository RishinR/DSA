from collections import deque


class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def solve(node):
    if not node:
        return 0

    if not node.left:
        return 1 + solve(node.right)
    if not node.right:
        return 1 + solve(node.left)

    return min(solve(node.right), solve(node.left)) + 1


def main():
    one = Node(1)
    two = Node(2)
    three = Node(3)
    four = Node(4)
    five = Node(5)
    six = Node(6)
    seven = Node(7)
    eight = Node(8)
    nine = Node(9)
    ten = Node(10)

    one.left = two
    one.right = eight
    two.left = three
    two.right = six
    eight.left = nine
    three.left = four
    three.right = five
    six.left = seven
    four.left = ten

    result = solve(one)
    print(result)


if __name__ == "__main__":
    main()
