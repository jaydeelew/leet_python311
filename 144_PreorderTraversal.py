# 144. Binary Tree Preorder Traversal (iterative)
# Given the root of a binary tree, return the preorder traversal of its nodes' values.


def preOrderIterative(root):
    # since iterative, we make use of a local stack
    stack = [root]
    ans = []

    while stack:
        node = stack.pop()

        # pre-order since print is prior to calls to left and right
        ans.append(node.val)

        # on iterative approach, swap left & right order so that left pops from stack first
        if node.right:
            stack.append(node.right)
        if node.left:
            stack.append(node.left)

    return ans


def preOrderRecursive(root):

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


class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


nine = TreeNode(9)
seven = TreeNode(7)
four = TreeNode(4)
eight = TreeNode(8, nine)
twelve = TreeNode(12, four)
three = TreeNode(3, twelve, seven)
five = TreeNode(5, eight, three)  # root node

print(preOrderIterative(five))  # Output: [5, 8, 9, 3, 12, 4, 7]
print(preOrderRecursive(five))  # Output: [5, 8, 9, 3, 12, 4, 7]
