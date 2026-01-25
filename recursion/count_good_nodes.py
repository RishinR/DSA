# leetcode 1448
class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def main():
    def count_good_nodes(node, prev):
        if not node:
            return 0

        if node.val >= prev:
            prev = node.val
            result[0] += 1

        count_good_nodes(node.left, prev)
        count_good_nodes(node.right, prev)

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

    result = [0]
    count_good_nodes(one, float("-inf"))
    print(result[0])


if __name__ == "__main__":
    main()
