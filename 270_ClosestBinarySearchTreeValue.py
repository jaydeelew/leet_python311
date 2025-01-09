# 270. Closest Binary Search Tree Value
# Given the root of a binary search tree and a target value, return the value in the BST that is closest to the target.
# Given target value is a floating point.
# You are guaranteed to have only one unique value in the BST that is closest to the target.
from typing import Optional


class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class BST:
    def closestValue(self, root: Optional[TreeNode], target: float) -> int:
        if not root:
            return None
        closest = root.val

        def helper(node, min_diff):
            # this allows the samel-named variable in enclosing function to be modified
            nonlocal closest
            # if two nodes have same difference from target, choose the smaller value
            if abs(target - node.val) == min_diff:
                closest = min(closest, node.val)
            if abs(target - node.val) < min_diff:
                min_diff = abs(target - node.val)
                closest = node.val
            if node.left:
                helper(node.left, min_diff)
            if node.right:
                helper(node.right, min_diff)

        helper(root, float("inf"))
        return closest


one = TreeNode(1)
three = TreeNode(3)
five = TreeNode(5)
two = TreeNode(2, one, three)
four = TreeNode(4, two, five)  # root

bst = BST()
print(bst.closestValue(four, 2.2))  # Output: 2
