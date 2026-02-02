# leetcode 99
from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def recoverTree(self, root: Optional[TreeNode]) -> None:
        nodes = []

        def inorder(node):
            if not node:
                return
            inorder(node.left)
            nodes.append(node)
            inorder(node.right)

        inorder(root)

        first = second = None

        for i in range(1, len(nodes)):
            if nodes[i - 1].val > nodes[i].val:
                if not first:
                    first = nodes[i - 1]
                second = nodes[i]

        # swap values
        first.val, second.val = second.val, first.val
