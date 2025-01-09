# 199. Binary Tree Right Side View
# Given the root of a binary tree, imagine yourself standing on the right side of it,
# return the values of the nodes you can see ordered from top to bottom.
from typing import Optional
from collections import deque


class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class BinaryBFS:
    def rightSideView(self, root: Optional[TreeNode]) -> list[int]:
        if not root:
            return []
        ans = []
        queue = deque([root])

        while queue:
            num_of_nodes_this_level = len(queue)
            # Append the value of the last node in this level
            ans.append(queue[-1].val)

            for _ in range(num_of_nodes_this_level):
                cur_node = queue.popleft()

                if cur_node.left:
                    queue.append(cur_node.left)
                if cur_node.right:
                    queue.append(cur_node.right)
        return ans


bfs = BinaryBFS()

nine = TreeNode(9)
seven = TreeNode(7)
four = TreeNode(4)
eight = TreeNode(8, nine)
twelve = TreeNode(12, four)
three = TreeNode(3, twelve, seven)
five = TreeNode(5, eight, three)  # root node

print(bfs.rightSideView(five))  # Output: [5, 3, 7, 4]
