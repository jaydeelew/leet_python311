from typing import Optional


class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class BinaryDFS:
    def dfs_pre_order(self, root):
        if not root:
            return
        print(root.val, end=" ")  # pre-order logic here
        self.dfs_pre_order(root.left)
        self.dfs_pre_order(root.right)
        return ""  # return "" necessary for not printing "None" at function return

    def dfs_in_order(self, root):
        if not root:
            return
        self.dfs_in_order(root.left)
        print(root.val, end=" ")  # in-order logic here
        self.dfs_in_order(root.right)
        return ""  # return "" necessary for not printing "None" at function return

    def dfs_post_order(self, root):
        if not root:
            return
        self.dfs_post_order(root.left)
        self.dfs_post_order(root.right)
        print(root.val, end=" ")  # post-order logic here
        return ""  # return "" necessary for not printing "None" at function return

    def dfs_pre_order_iterative(self, root):
        if not root:
            return
        stack = [root]
        while stack:
            node = stack.pop()
            print(node.val, end=" ")
            # on iterative approach, swap left & right order so that left pops from stack first
            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)
        return ""  # return "" necessary for not printing "None" at function return


dfs = BinaryDFS()

nine = TreeNode(9)
seven = TreeNode(7)
four = TreeNode(4)
eight = TreeNode(8, nine)
twelve = TreeNode(12, four)
three = TreeNode(3, twelve, seven)
five = TreeNode(5, eight, three)  # root node

print(dfs.dfs_pre_order(five))
print(dfs.dfs_in_order(five))
print(dfs.dfs_post_order(five))
print(dfs.dfs_pre_order_iterative(five))
