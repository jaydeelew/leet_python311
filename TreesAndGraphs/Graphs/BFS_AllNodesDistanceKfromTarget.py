# 863. All Nodes Distance K in Binary Tree
# Given the root of a binary tree, a target node target in the tree, and an integer k,
# return an array of the values of all nodes that have a distance k from the target node.
from collections import deque


class TreeNode:
    def __init__(self, val, left=None, right=None) -> None:
        self.val = val
        self.parent = None
        self.left = left
        self.right = right


class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> list[int]:
        # this DFS takes a binary tree (which is a directed graph) and makes it an undirected graph by adding parent to each node
        def dfs(node, parent):
            if not node:
                return

            node.parent = parent
            dfs(node.left, node)
            dfs(node.right, node)

        dfs(root, None)  # add all parents starting at root (root has None for parent)

        queue = deque([target])  # we use tardet node as start of our BFS to level k
        seen = {target}
        distance = 0
        # now for BFS
        while queue and distance < k:
            current_length = len(queue)
            for _ in range(current_length):
                node = queue.popleft()
                for neighbor in [node.left, node.right, node.parent]:  # this allows to to move up and down the tree
                    if neighbor and neighbor not in seen:
                        seen.add(neighbor)
                        queue.append(neighbor)

            distance += 1
        # once distance == k, we return the values in the queue
        return [node.val for node in queue]


sol = Solution()

six = TreeNode(6)
seven = TreeNode(7)
four = TreeNode(4)
zero = TreeNode(0)
eight = TreeNode(8)
two = TreeNode(2, seven, four)
five = TreeNode(5, six, two)
one = TreeNode(1, zero, eight)
three = TreeNode(3, five, one)  # root node

root = three
target = five
k = 2  # Output: [7,4,1]

print(sol.distanceK(root, target, k))
