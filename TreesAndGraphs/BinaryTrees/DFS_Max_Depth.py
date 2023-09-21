from typing import Optional


class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class BinaryDFS:
    # Given the root of a binary tree, find the length of the longest path from the root to a leaf.
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        left = self.maxDepth(root.left)  # left is assigned node count thus far from children on left tree
        right = self.maxDepth(root.right)  # left is assigned node count thus far from children on right tree
        return max(left, right) + 1  # return max of left vs right children + 1 for this node

    def maxDepthIterative(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        stack = [(root, 1)]  # place tuple w/ root node object and integer 1 on the stack
        ans = 0
        while stack:
            node, depth = stack.pop()  # pop tuple with node object and integer with depth
            ans = max(ans, depth)  # assign ans the greater of previous answer and depth of top of stack
            if node.right:
                stack.append((node.right, depth + 1))  # if there is a right node, push it on stack and increment depth
            if node.left:
                stack.append((node.left, depth + 1))  # if there is a left node, push it on stack and increment depth
        return ans


dfs = BinaryDFS()

nine = TreeNode(9)
seven = TreeNode(7)
four = TreeNode(4)
eight = TreeNode(8, nine)
twelve = TreeNode(12, four)
three = TreeNode(3, twelve, seven)
five = TreeNode(5, eight, three)  # root node

print(dfs.maxDepth(five))
print(dfs.maxDepthIterative(five))
