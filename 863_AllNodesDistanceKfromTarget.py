# 863. All Nodes Distance K in Binary Tree
# Given the root of a binary tree, a target node target in the tree, and an integer k,
# return an array of the values of all nodes that have a distance k from the target node.
from collections import deque


def distanceK(root, target, k) -> list[int]:
    # this DFS takes a binary tree (which is a directed graph) and makes it an undirected graph by adding parent to each node
    def dfs(node, parent):
        if not node:
            return

        node.parent = parent
        dfs(node.left, node)
        dfs(node.right, node)

    # add all parents starting at root (root has None for parent)
    dfs(root, None)

    # we use tardet node as start of our BFS to level k
    queue = deque([target])
    seen = {target}
    distance = 0
    # now for BFS
    while queue and distance < k:
        current_length = len(queue)
        # iterate over number of nodes at each level
        for _ in range(current_length):
            # all nodes will be popped from current level at last iteration
            node = queue.popleft()
            # this allows us to move up and down the tree
            for neighbor in [node.left, node.right, node.parent]:
                if neighbor and neighbor not in seen:
                    seen.add(neighbor)
                    queue.append(neighbor)

        # after a level is popped from queue, distance is incremented
        distance += 1
    # once distance == k, we return the values in the queue
    return [node.val for node in queue]  # list comprehension


class TreeNode:
    def __init__(self, val, left=None, right=None) -> None:
        self.val = val
        self.parent = None
        self.left = left
        self.right = right


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

print(distanceK(root, target, k))
