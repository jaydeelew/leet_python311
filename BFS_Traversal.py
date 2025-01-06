from typing import Optional
from collections import deque


class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class BST:
    def BFStraversal(self, root: Optional[TreeNode]):
        queue = deque([root])
        while queue:
            num_nodes_in_tree_level = len(queue)
            for _ in range(num_nodes_in_tree_level):
                node = queue.popleft()
                print(node.val, end=" ")
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)


one = TreeNode(1)
three = TreeNode(3)
five = TreeNode(5)
two = TreeNode(2, one, three)
four = TreeNode(4, two, five)  # root

bst = BST()
print(bst.BFStraversal(four))  # Output: 4 2 5 1 3 None
