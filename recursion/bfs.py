from collections import deque

class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def bfs(node):
    if not node:
        return []
    q = deque([node])
    result = []
    while q:
        curr_len = len(q)
        output = []
        for _ in range(curr_len):
            curr_node = q.popleft()
            output.append(curr_node.val)
            if curr_node.left:
                q.append(curr_node.left)
            if curr_node.right:
                q.append(curr_node.right)
        result.append(output)
    print(result)

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

    bfs(one)


if __name__ == "__main__":
    main()
