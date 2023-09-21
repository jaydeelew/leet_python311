from typing import Optional
from collections import deque


class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class BinaryBFS:
    # Given the root of a binary tree, return the zigzag level order traversal of its nodes' values.
    # (i.e., from left to right, then right to left for the next level and alternate between).
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> list[list[int]]:
        if not root:
            return []
        ans = []
        queue = deque([root])
        reverse = True
        while queue:
            level = []
            level_length = len(queue)
            if reverse is True:
                reverse = False
            else:
                reverse = True
            for _ in range(level_length):
                node = queue.popleft()
                if reverse is False:
                    level.append(node.val)
                else:
                    level.insert(0, node.val)  # insert at the beginning of list to reverse order
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            ans.append(level)
        return ans


bfs = BinaryBFS()

nine = TreeNode(9)
seven = TreeNode(7)
four = TreeNode(4)
eight = TreeNode(8, nine)
twelve = TreeNode(12, four)
three = TreeNode(3, twelve, seven)
five = TreeNode(5, eight, three)  # root node

print(bfs.zigzagLevelOrder(five))
print("")
