from typing import Optional
from collections import deque


class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class BinaryBFS:
    def print_all_nodes(self, root):
        queue = deque([root])  # [root], and not "root" alone, is necessary since deque requires an iterable
        while queue:
            nodes_in_current_level = len(queue)
            # do some logic here for the current level

            for _ in range(nodes_in_current_level):
                node = queue.popleft()

                # do some logic here on the current node
                print(node.val, end=" ")

                # put the next level onto the queue
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

    # Given the root of a binary tree, imagine yourself standing on the right side of it.
    # Return the values of the nodes you can see ordered from top to bottom.
    def rightSideView(self, root: Optional[TreeNode]) -> list[int]:
        if not root:
            return []
        ans = []
        queue = deque([root])
        while queue:
            num_of_nodes_this_level = len(queue)
            # do some logic here for the current level
            ans.append(queue[-1].val)

            for _ in range(num_of_nodes_this_level):
                cur_node = queue.popleft()
                # do some logic here on the current node

                # put the next level onto the queue
                if cur_node.left:
                    queue.append(cur_node.left)
                if cur_node.right:
                    queue.append(cur_node.right)
        return ans

    # Given the root of a binary tree, return an array of the largest value in each row of the tree.
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

    # Given the root of a binary tree, return the sum of values of its deepest leaves.
    def deepestLeavesSum(self, root: Optional[TreeNode]) -> int:
        queue = deque([root])
        level_sum = 0
        while queue:
            level_sum = 0
            for _ in range(len(queue)):
                node = queue.popleft()
                level_sum += node.val
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
        return level_sum

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
