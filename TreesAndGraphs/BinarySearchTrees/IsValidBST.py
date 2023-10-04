from typing import Optional


class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class BST:
    # 98. Validate Binary Search Tree
    # Given the root of a binary tree, determine if it is a valid BST.
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def dfs(node, small, large):
            if not node:
                return True  # if there is no node, it does not invalidate a BST
            # first call to function with node val between -inf & inf
            if not (small < node.val < large):
                return False
            # call to left child uses parent's small, and uses current/parent node value as large
            left = dfs(node.left, small, node.val)
            # call to right child uses parent's large, and uses current/parent node value as small
            right = dfs(node.right, node.val, large)

            # tree is a BST if left and right subtrees are also BSTs
            return left and right

        return dfs(root, float("-inf"), float("inf"))

    def isValidBST_Iterative(self, root: Optional[TreeNode]) -> bool:
        stack = [(root, float("-inf"), float("inf"))]
        while stack:
            node, small, large = stack.pop()
            if not (small < node.val < large):
                return False
            # if left child exists, append tuple of left child's val, parent's small , and current/parent node value as large
            if node.left:
                stack.append((node.left, small, node.val))
            # if right child exists, append tuple of right child's val, parent's large , and current/parent node value as small
            if node.right:
                stack.append((node.right, node.val, large))
        return True


one = TreeNode(1)
three = TreeNode(3)
five = TreeNode(5)
two = TreeNode(2, one, three)
four = TreeNode(4, two, five)  # root

bst = BST()
print(bst.isValidBST(four))
print(bst.isValidBST_Iterative(four))
