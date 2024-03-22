# def dfs(root):
#     stack = [root]
#     ans = 0

#     while stack:
#         node = stack.pop()
#         # do logic
#         if node.left:
#             stack.append(node.left)
#         if node.right:
#             stack.append(node.right)

#     return ans


# print the nodes of a binary tree using DFS in pre-order, iteratively


class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def dfs_pre_order(root):
    if not root:
        return

    ans = []
    # since iterative, we create make use of local stack
    stack = [root]

    while stack:
        node = stack.pop()
        ans.append(node.val)

        # on iterative approach, swap left & right order so that left pops from stack first
        if node.right:
            stack.append(node.right)
        if node.left:
            stack.append(node.left)

    return ans


nine = TreeNode(9)
seven = TreeNode(7)
four = TreeNode(4)
eight = TreeNode(8, nine)
twelve = TreeNode(12, four)
three = TreeNode(3, twelve, seven)
five = TreeNode(5, eight, three)  # root node

print(dfs_pre_order(five))  # Output: 5 8 9 3 12 4 7
