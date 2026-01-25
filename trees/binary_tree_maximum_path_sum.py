# leetcode 543
from collections import deque


class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def main():
    def max_savings(node):
        if not node:
            return 0
        left_savings = max(0, max_savings(node.left))
        right_savings = max(0, max_savings(node.right))
        result[0] = max(result[0], node.val + left_savings + right_savings)
        return node.val + max(left_savings, right_savings)

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

    result = [float("-inf")]
    max_savings(one)
    print(result[0])


if __name__ == "__main__":
    main()
