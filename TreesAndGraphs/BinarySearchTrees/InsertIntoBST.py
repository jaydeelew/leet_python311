# 701. You are given the root node of a binary search tree (BST) and a value to insert into the tree.
# Return the root node of the BST after the insertion. It is guaranteed that the new value does not exist in the original BST.
# Notice that there may exist multiple valid ways for the insertion, as long as the tree remains a BST after insertion.
# You can return any of them.
from typing import Optional


class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class BST:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        node_to_insert = TreeNode(val)
        if not root:
            return node_to_insert

        def helper(node):
            if val < node.val:
                if not node.left:
                    node.left = node_to_insert
                    return
                else:
                    helper(node.left)
            else:
                if not node.right:
                    node.right = node_to_insert
                    return
                else:
                    helper(node.right)

        helper(root)
        return root

    def insertIntoBST_Iterarive(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        node_to_insert = TreeNode(val)
        if not root:
            return node_to_insert
        stack = [root]
        while stack:
            node = stack.pop()
            if val < node.val:
                if node.left is None:
                    node.left = node_to_insert
                    return root
                else:
                    stack.append(node.left)
            else:
                if node.right is None:
                    node.right = node_to_insert
                    return root
                else:
                    stack.append(node.right)


one = TreeNode(1)
three = TreeNode(3)
five = TreeNode(5)
two = TreeNode(2, one, three)
four = TreeNode(4, two, five)  # root

bst = BST()
print(bst.insertIntoBST(four, 3.5).val)  # Output: 4
print(bst.insertIntoBST_Iterarive(four, 3.5).val)  # Output: 4
