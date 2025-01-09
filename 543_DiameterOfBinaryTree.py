# 543. Diameter of Binary Tree
# Given the root of a binary tree, return the length of the diameter of the tree.
# The diameter of a binary tree is the length of the longest path between any two nodes in a tree.
# This path may or may not pass through the root.
# The length of a path between two nodes is represented by the number of edges between them.
from typing import Optional


class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class BinaryDFS:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        self.max_edges = 0

        def helper(node):
            if not node:
                return 0
            left = helper(node.left)
            right = helper(node.right)
            self.max_edges = max(self.max_edges, left + right)
            return max(left, right) + 1

        helper(root)
        return self.max_edges


dfs = BinaryDFS()

nine = TreeNode(9)
seven = TreeNode(7)
four = TreeNode(4)
eight = TreeNode(8, nine)
twelve = TreeNode(12, four)
three = TreeNode(3, twelve, seven)
five = TreeNode(5, eight, three)  # root node

print(dfs.diameterOfBinaryTree(five))  # Output: 5
