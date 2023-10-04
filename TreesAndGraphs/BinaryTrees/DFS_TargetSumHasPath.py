from typing import Optional


class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class BinaryDFS:
    # Given the root of a binary tree and an integer targetSum, return true if there exists a path from the root
    # to a leaf such that the sum of the nodes on the path is equal to targetSum, and return false otherwise.
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if not root:
            return False
        remainder = targetSum - root.val
        if not root.left and not root.right:  # if both children are null, then the node is a leaf
            return remainder == 0
        left = self.hasPathSum(root.left, remainder)
        right = self.hasPathSum(root.right, remainder)
        return left or right

    # def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
    #     def dfs(node, curr):
    #         if not node:
    #             return False
    #         # if both children are null, then the node is a leaf
    #         if node.left is None and node.right is None:
    #             return (curr + node.val) == targetSum
    #         curr += node.val
    #         left = dfs(node.left, curr)
    #         right = dfs(node.right, curr)
    #         return left or right


dfs = BinaryDFS()

nine = TreeNode(9)
seven = TreeNode(7)
four = TreeNode(4)
eight = TreeNode(8, nine)
twelve = TreeNode(12, four)
three = TreeNode(3, twelve, seven)
five = TreeNode(5, eight, three)  # root node
print(dfs.hasPathSum(five, 24))  # return True

# two = TreeNode(2)
# one = TreeNode(1, two)  # root node
# print(dfs.hasPathSum(one, 1))  # return False
