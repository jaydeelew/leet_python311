# 515. Find Largest Value in Each Tree Row
# Given the root of a binary tree, return an array of the largest value in each row of the tree (0-indexed).
from typing import Optional
from collections import deque


class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class BinaryBFS:
    def largestValues(self, root: Optional[TreeNode]) -> list[int]:
        if not root:
            return []
        ans = []
        queue = deque([root])
        while queue:
            num_nodes_in_level = len(queue)
            max_val_in_row = float("-inf")
            for _ in range(num_nodes_in_level):
                node = queue.popleft()
                max_val_in_row = max(max_val_in_row, node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            ans.append(max_val_in_row)
        return ans


bfs = BinaryBFS()

nine = TreeNode(9)
seven = TreeNode(7)
four = TreeNode(4)
eight = TreeNode(8, nine)
twelve = TreeNode(12, four)
three = TreeNode(3, twelve, seven)
five = TreeNode(5, eight, three)  # root node

print(bfs.largestValues(five))  # Output: [5, 8, 12, 4]
