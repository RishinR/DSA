# leetcode 110
class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def balanced_tree(node):
    if not node:
        return 0

    left_h = balanced_tree(node.left)
    if left_h == -1:
        return -1
    
    right_h = balanced_tree(node.right)
    if right_h == -1:
        return -1
    
    if abs(left_h - right_h) > 1:
        return -1
    
    return 1 + max(left_h, right_h)

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

    print(balanced_tree(one) != -1)
    

if __name__ == "__main__":
    main()