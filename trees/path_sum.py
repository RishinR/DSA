from collections import deque


class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def solve(node, curr_sum):
    if not node:
        return

    curr_sum += node.val
    if not node.left and not node.right:
        print(node.val, curr_sum)
        return

    solve(node.left, curr_sum)
    solve(node.right, curr_sum)


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

    solve(one, 0)


if __name__ == "__main__":
    main()
