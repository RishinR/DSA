# leetcode 987
class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def vertical_order_traversal(root):
    nodes = []

    def dfs(row, col, node):
        if node:
            nodes.append((col, row, node.val))
            dfs(row + 1, col - 1, node.left)
            dfs(row + 1, col + 1, node.right)
    dfs(0, 0, root)

    nodes.sort()

    result = []
    prev = float('-inf')
    for col, row, node in nodes:
        if col > prev:
            prev = col
            result.append([node])
        elif col == prev:
            result[-1].append(node)
    return result

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

    result = vertical_order_traversal(one)
    print(result)
    

if __name__ == "__main__":
    main()