# Trivia to know: an in-order DFS traversal prioritizing left before right on a BST will handle the nodes in sorted order.
from typing import Optional


class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class BST:
    def DFSinOrderTraversal(self, root: Optional[TreeNode]):
        if not root:
            return
        if root.left:
            self.DFSinOrderTraversal(root.left)
        # here is the "in-order" print statement between calls to left and right nodes
        print(root.val, end=" ")
        if root.right:
            self.DFSinOrderTraversal(root.right)
        # return "" necessary for not printing "None" at last stack return
        return ""


one = TreeNode(1)
three = TreeNode(3)
five = TreeNode(5)
two = TreeNode(2, one, three)
four = TreeNode(4, two, five)  # root

bst = BST()
print(bst.DFSinOrderTraversal(four))  # Output: 1 2 3 4 5
