# 938: Range Sum of BST
# Given the root node of a binary search tree and two integers low and high,
# return the sum of values of all nodes with a value in the inclusive range [low, high].
from typing import Optional


class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class BST:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        if not root:
            return 0
        ans = 0
        # if this node's value falls within the low to high range (inclusive), add it to sum
        if low <= root.val <= high:
            ans += root.val
        # if low val is less than the current node's val, there might be another node in left subtree
        if low < root.val:
            ans += self.rangeSumBST(root.left, low, high)
        # if high val is greater than the current node's val, there might be another node in right subtree
        if root.val < high:
            ans += self.rangeSumBST(root.right, low, high)
        return ans

    def rangeSumBST_Iterative(self, root: Optional[TreeNode], low: int, high: int) -> int:
        stack = [root]
        ans = 0
        while stack:
            node = stack.pop()
            if low <= node.val <= high:
                ans += node.val
            if node.left and low < node.val:
                stack.append(node.left)
            if node.right and high > node.val:
                stack.append(node.right)
        return ans


one = TreeNode(1)
three = TreeNode(3)
five = TreeNode(5)
two = TreeNode(2, one, three)
four = TreeNode(4, two, five)  # root

bst = BST()
print(bst.rangeSumBST(four, 2, 4))  # Output: 9
print(bst.rangeSumBST_Iterative(four, 2, 4))  # Output: 9
