# 1302. Deepest Leaves Sum
# Given the root of a binary tree, return the sum of values of its deepest leaves.
from collections import deque


def deepestLeavesSum(root):
    if not root:
        return 0

    q = deque([root])

    while q:
        sz = len(q)
        level_sum = 0

        for _ in range(sz):
            node = q.popleft()
            level_sum += node.val

            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)

    return level_sum


class TreeNode:
    def __init__(self, val, left=None, right=None) -> None:
        self.val = val
        self.left = left
        self.right = right


nine = TreeNode(9)
four = TreeNode(4)
two = TreeNode(2)
thirteen = TreeNode(13)
seven = TreeNode(7, two, thirteen)
eight = TreeNode(8, nine)
twelve = TreeNode(12, four)
three = TreeNode(3, twelve, seven)
five = TreeNode(5, eight, three)  # root node

print(deepestLeavesSum(five))
# Output: 19
