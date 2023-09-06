from typing import Optional
from collections import deque


class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class BST:
    # Trivia to know: an inorder DFS traversal prioritizing left before right on a BST will handle the nodes in sorted order.
    def DFSinOrderTraversal(self, root: Optional[TreeNode]):
        if not root:
            return
        if root.left:
            self.DFSinOrderTraversal(root.left)
        print(root.val, end=" ")
        if root.right:
            self.DFSinOrderTraversal(root.right)
        return ""  # return "" necessary for not printing "None" at last stack return

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

    # 938: Range Sum of BST
    # Given the root node of a binary search tree and two integers low and high,
    # return the sum of values of all nodes with a value in the inclusive range [low, high].
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        if not root:
            return 0
        ans = 0
        if low <= root.val <= high:  # if this node's value falls within the low to high range (inclusive), add it to sum
            ans += root.val
        if low < root.val:  # if low val is less than the current node's val, there might be another node in left subtree
            ans += self.rangeSumBST(root.left, low, high)
        if root.val < high:  # if high val is greater than the current node's val, there might be another node in right subtree
            ans += self.rangeSumBST(root.right, low, high)
        return ans

    def rangeSumBST_Iterative(self, root: Optional[TreeNode], low: int, high: int) -> int:
        stack = [root]
        ans = 0
        while stack:
            node = stack.pop()
            if low <= node.val <= high:
                ans += node.val
            if node.left and low < node.val:
                stack.append(node.left)
            if node.right and high > node.val:
                stack.append(node.right)
        return ans

    # 530. Minimum Absolute Difference in BST
    # Given the root of a BST, return the minimum absolute difference between the values of any two different nodes in the tree.
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        def dfs(node):
            if not node:
                return
            dfs(node.left)
            values.append(node.val)
            dfs(node.right)

        values = []
        dfs(root)
        ans = float("inf")
        for i in range(1, len(values)):
            ans = min(ans, values[i] - values[i - 1])
        return ans

    # 98. Validate Binary Search Tree
    # Given the root of a binary tree, determine if it is a valid BST.
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def dfs(node, small, large):
            if not node:
                return True  # if there is no node, it does not invalidate a BST
            # first call to function with node val between -inf & inf
            if not (small < node.val < large):
                return False
            # call to left child uses parent's small, and uses current/parent node value as large
            left = dfs(node.left, small, node.val)
            # call to right child uses parent's large, and uses current/parent node value as small
            right = dfs(node.right, node.val, large)

            # tree is a BST if left and right subtrees are also BSTs
            return left and right

        return dfs(root, float("-inf"), float("inf"))

    def isValidBST_Iterative(self, root: Optional[TreeNode]) -> bool:
        stack = [(root, float("-inf"), float("inf"))]
        while stack:
            node, small, large = stack.pop()
            if not (small < node.val < large):
                return False
            # if left child exists, append tuple of left child's val, parent's small , and current/parent node value as large
            if node.left:
                stack.append((node.left, small, node.val))
            # if right child exists, append tuple of right child's val, parent's large , and current/parent node value as small
            if node.right:
                stack.append((node.right, node.val, large))
        return True

    # You are given the root node of a binary search tree (BST) and a value to insert into the tree.
    # Return the root node of the BST after the insertion. It is guaranteed that the new value does not exist in the original BST.
    # Notice that there may exist multiple valid ways for the insertion, as long as the tree remains a BST after insertion.
    # You can return any of them.
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        node_to_insert = TreeNode(val)
        if not root:
            return node_to_insert

        def helper(node):
            if val < node.val:
                if not node.left:
                    node.left = node_to_insert
                    return
                else:
                    helper(node.left)
            else:
                if not node.right:
                    node.right = node_to_insert
                    return
                else:
                    helper(node.right)

        helper(root)
        return root

    def insertIntoBST_Iterarive(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        node_to_insert = TreeNode(val)
        if not root:
            return node_to_insert
        stack = [root]
        while stack:
            node = stack.pop()
            if val < node.val:
                if node.left is None:
                    node.left = node_to_insert
                    return root
                else:
                    stack.append(node.left)
            else:
                if node.right is None:
                    node.right = node_to_insert
                    return root
                else:
                    stack.append(node.right)

    # Given the root of a binary search tree and a target value, return the value in the BST that is closest to the target.
    # If there are multiple answers, print the smallest.
    def closestValue(self, root: Optional[TreeNode], target: float) -> int:
        if not root:
            return None
        closest = root.val

        def helper(node, min_diff):
            nonlocal closest  # this allows the samel-named variable in enclosing function to be modified
            if abs(target - node.val) == min_diff:  # if two nodes have same difference from target, choose the smaller value
                closest = min(closest, node.val)
            if abs(target - node.val) < min_diff:
                min_diff = abs(target - node.val)
                closest = node.val
            if node.left:
                helper(node.left, min_diff)
            if node.right:
                helper(node.right, min_diff)

        helper(root, float("inf"))
        return closest


# three = TreeNode(3)
# seven = TreeNode(7)
# eighteen = TreeNode(18)
# five = TreeNode(5, three, seven)
# fifteen = TreeNode(15, right=eighteen)
# ten = TreeNode(10, five, fifteen)  # root

# four = TreeNode(4)
# three = TreeNode(3)
# seven = TreeNode(7)
# six = TreeNode(6, three, seven)
# five = TreeNode(5, four, six)  # root

# one = TreeNode(1)
# three = TreeNode(3)
# seven = TreeNode(7)
# two = TreeNode(2, one, three)
# four = TreeNode(4, two, seven)  # root

one = TreeNode(1)
three = TreeNode(3)
five = TreeNode(5)
two = TreeNode(2, one, three)
four = TreeNode(4, two, five)  # root

bst = BST()
print(bst.closestValue(four, 3.5))
