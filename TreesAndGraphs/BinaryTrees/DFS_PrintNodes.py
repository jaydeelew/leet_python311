# print the nodes of a binary tree using DFS in pre-order, in-order, and post-order traveral


class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class BinaryDFS:
    def dfs_pre_order(self, root):
        if not root:
            return
        # pre-order logic here
        print(root.val, end=" ")
        self.dfs_pre_order(root.left)
        self.dfs_pre_order(root.right)
        # return "" necessary for not printing "None" at function return
        return ""

    def dfs_in_order(self, root):
        if not root:
            return
        self.dfs_in_order(root.left)
        # in-order logic here
        print(root.val, end=" ")
        self.dfs_in_order(root.right)
        # return "" necessary for not printing "None" at function return
        return ""

    def dfs_post_order(self, root):
        if not root:
            return
        self.dfs_post_order(root.left)
        self.dfs_post_order(root.right)
        # post-order logic here
        print(root.val, end=" ")
        # return "" necessary for not printing "None" at function return
        return ""

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
        # return "" necessary for not printing "None" at function return
        return ""


dfs = BinaryDFS()

nine = TreeNode(9)
seven = TreeNode(7)
four = TreeNode(4)
eight = TreeNode(8, nine)
twelve = TreeNode(12, four)
three = TreeNode(3, twelve, seven)
five = TreeNode(5, eight, three)  # root node

print(dfs.dfs_pre_order(five))  # Output: 5 8 9 3 12 4 7
print(dfs.dfs_in_order(five))  # Output: 9 8 5 4 12 3 7
print(dfs.dfs_post_order(five))  # Output: 9 8 4 12 7 3 5
print(dfs.dfs_pre_order_iterative(five))  # Output: 5 8 9 3 12 4 7
