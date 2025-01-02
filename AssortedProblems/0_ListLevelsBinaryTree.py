# 0. List Levels Binary Tree
# Given the root of a binary tree, return the levels of the tree from root on down in a list of lists.
from collections import deque


def listLevels(root):
    # [root], and not "root" alone, is necessary since deque requires an iterable
    queue = deque([root])
    ans = []

    while queue:
        # queue stores ListNode objects, so we use list comprehension to extract values.
        ans.append([node.val for node in queue])

        num_of_nodes_curr_level = len(queue)

        for _ in range(num_of_nodes_curr_level):
            node = queue.popleft()

            # putting next level onto the queue with completion of for loop
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

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

print(listLevels(five))
# Output: [[5], [8, 3], [9, 12, 7], [4]]
