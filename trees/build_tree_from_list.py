class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def dfs(root: Node | None):
    if not root:
        return

    dfs(root.left)
    print(root.val)
    dfs(root.right)


def main():
    tree_list = [
        1,
        2, 6,
        3, None, None, 7,
        4, 5, None, None, None, None, 8, 9,
        None, None, None, None, None, None, None, None,
        None, None, None, None,
        10
    ]

    tree = []

    # Create all nodes
    for value in tree_list:
        if value is None:
            tree.append(None)
        else:
            tree.append(Node(value))

    # Connect nodes
    for index in range(len(tree)):
        if tree[index] is None:
            continue

        left = 2 * index + 1
        right = 2 * index + 2

        if left < len(tree):
            tree[index].left = tree[left]

        if right < len(tree):
            tree[index].right = tree[right]

    # Inorder traversal
    dfs(tree[0])


if __name__ == "__main__":
    main()