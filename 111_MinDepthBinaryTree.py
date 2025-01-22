# 111. Given a binary tree, find its minimum depth.
# The minimum depth is the number of nodes along the shortest path from the root node down to the nearest leaf node.
# Note: A leaf is a node with no children.
from collections import deque


class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def minDepth(root):
    if not root:
        return 0

    queue = deque([root])
    depth = 0

    while queue:
        q_sz = len(queue)
        depth += 1

        for _ in range(q_sz):
            node = queue.popleft()

            if not node.left and not node.right:
                return depth

            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)


nine = TreeNode(9)
seven = TreeNode(7)
four = TreeNode(4)
eight = TreeNode(8, nine)
twelve = TreeNode(12, four)
three = TreeNode(3, twelve, seven)
five = TreeNode(5, eight, three)  # root node

print(minDepth(five))  # Output: 3
print(minDepth(None))  # Output: 0
