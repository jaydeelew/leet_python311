# def dfs(root):
#     if not root:
#         return

#     ans = 0

#     # do logic
#     dfs(root.left)
#     dfs(root.right)
#     return ans


# print the nodes of a binary tree using DFS in pre-order, recursively
class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def dfs_pre_order(root):

    def dfs(node):
        if node is None:
            return

        # pre-order since print is prior to calls to left and right
        ans.append(node.val)

        dfs(node.left)
        dfs(node.right)

    ans = []
    dfs(root)
    return ans


nine = TreeNode(9)
seven = TreeNode(7)
four = TreeNode(4)
eight = TreeNode(8, nine)
twelve = TreeNode(12, four)
three = TreeNode(3, twelve, seven)
five = TreeNode(5, eight, three)  # root node

print(dfs_pre_order(five))  # Output: [5, 8, 9, 3, 12, 4, 7]
