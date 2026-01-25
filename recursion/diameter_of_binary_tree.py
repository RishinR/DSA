# leetcode 543
from collections import deque

class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def main():
    def height(node):
        if not node:
            return 0
        
        left_h = height(node.left)
        right_h = height(node.right)
        
        result[0] = max(result[0], left_h + right_h)
        return 1 + max(left_h, right_h)

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
    height(one)
    print(result[0])


if __name__ == "__main__":
    main()
