# 104. Given the root of a binary tree, find the length of the longest path from the root to a leaf.
from typing import Optional


class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class BinaryDFS:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        # left is assigned node count thus far from children on left tree
        left = self.maxDepth(root.left)
        # left is assigned node count thus far from children on right tree
        right = self.maxDepth(root.right)
        # return max of left vs right children + 1 for this node
        return max(left, right) + 1

    def maxDepthIterative(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        # place tuple w/ root node object and integer 1 on the stack
        stack = [(root, 1)]
        ans = 0
        while stack:
            # pop tuple with node object and integer with depth
            node, depth = stack.pop()
            # assign ans the greater of previous answer and depth of top of stack
            ans = max(ans, depth)
            if node.right:
                # if there is a right node, push it on stack and increment depth
                stack.append((node.right, depth + 1))
            if node.left:
                # if there is a left node, push it on stack and increment depth
                stack.append((node.left, depth + 1))
        return ans


dfs = BinaryDFS()

nine = TreeNode(9)
seven = TreeNode(7)
four = TreeNode(4)
eight = TreeNode(8, nine)
twelve = TreeNode(12, four)
three = TreeNode(3, twelve, seven)
five = TreeNode(5, eight, three)  # root node

print(dfs.maxDepth(five))  # Output: 4
print(dfs.maxDepthIterative(five))  # Output: 4
