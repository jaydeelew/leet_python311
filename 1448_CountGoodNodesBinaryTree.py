# 1448. Count Good Nodes in Binary Tree
# Given the root of a binary tree, find the number of nodes that are good. A node is good if the path between the root
# and the node has no nodes with a greater value.
from typing import Optional


class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class BinaryDFS:
    def goodNodes(self, root: Optional[TreeNode], maxSoFar: Optional[float] = float("-inf")) -> int:
        if not root:
            return 0
        good = 0
        # the original root will be counted in total number of good nodes
        if root.val >= maxSoFar:
            maxSoFar = root.val
            good = 1
        left = self.goodNodes(root.left, maxSoFar)
        right = self.goodNodes(root.right, maxSoFar)
        return left + right + good

    # def goodNodes(self, root: TreeNode) -> int:
    #     def dfs(node, max_so_far):
    #         if not node:
    #             return 0
    #         left = dfs(node.left, max(max_so_far, node.val))
    #         right = dfs(node.right, max(max_so_far, node.val))
    #         ans = left + right
    #         # the original root will be counted in total number of good nodes
    #         if node.val >= max_so_far:
    #             ans += 1
    #         return ans

    #     return dfs(root, float("-inf"))


dfs = BinaryDFS()

ten = TreeNode(10)
nine = TreeNode(9)
seven = TreeNode(7)
four = TreeNode(4)
eight = TreeNode(8, nine)
twelve = TreeNode(12, four, ten)
three = TreeNode(3, twelve, seven)
five = TreeNode(5, eight, three)  # root node

print(dfs.goodNodes(five))  # Output: 5
