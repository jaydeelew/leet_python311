# 236. Lowest Common Ancestor of a Binary Tree
# Given the root of a binary tree and two nodes p and q that are in the tree, return the lowest common ancestor (LCA)
# of the two nodes. The LCA is the lowest node in the tree that has both p and q as descendants
# (note: a node is a descendant of itself).
from typing import Optional


class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class BinaryDFS:
    def lowestCommonAncestor(self, root: Optional["TreeNode"], p: "TreeNode", q: "TreeNode") -> Optional["TreeNode"]:
        if not root:
            return None
        if root == p or root == q:
            return root
        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)
        if left and right:
            return root
        # if not left and not right: # not needed since if function does not return, left/right will be None
        #     return None
        if left:
            return left
        return right


dfs = BinaryDFS()

nine = TreeNode(9)
seven = TreeNode(7)
four = TreeNode(4)
eight = TreeNode(8, nine)
twelve = TreeNode(12, four)
three = TreeNode(3, twelve, seven)
five = TreeNode(5, eight, three)  # root node

print(dfs.lowestCommonAncestor(five, four, seven).val)  # ".val" to print value to the returned node
# Output: 3
