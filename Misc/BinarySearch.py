from typing import Optional


class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class BinarySearch:
    def dfs(self, root):
        if not root:
            return
        print(root.val, end=" ")
        self.dfs(root.left)
        self.dfs(root.right)
        return ""  # return "" only necessary for not printing "None" at last stack return

    def dfsIterative(self, root):
        if not root:
            return
        stack = [root]
        while stack:
            node = stack.pop()
            print(node.val, end=" ")
            # on iterative approach, swap left & right order so that left pops from stack first
            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)
        return

    # Given the root of a binary tree, find the length of the longest path from the root to a leaf.
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        left = self.maxDepth(root.left)  # left is assigned node count thus far from children on left tree
        right = self.maxDepth(root.right)  # left is assigned node count thus far from children on right tree
        return max(left, right) + 1  # return max of left vs right children + 1 for this node

    def maxDepthIterative(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        stack = [(root, 1)]  # place tuple w/ root node object and integer 1 on the stack
        ans = 0
        while stack:
            node, depth = stack.pop()  # pop tuple with node object and integer with depth
            ans = max(ans, depth)  # assign ans the greater of previous answer and depth of top of stack
            if node.right:
                stack.append((node.right, depth + 1))  # if there is a right node, push it on stack and increment depth
            if node.left:
                stack.append((node.left, depth + 1))  # if there is a left node, push it on stack and increment depth
        return ans

    # Given the root of a binary tree and an integer targetSum, return true if there exists a path from the root
    # to a leaf such that the sum of the nodes on the path is equal to targetSum, and return false otherwise.
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if not root:
            return False
        remainder = targetSum - root.val
        if not root.left and not root.right:  # if both children are null, then the node is a leaf
            return remainder == 0
        left = self.hasPathSum(root.left, remainder)
        right = self.hasPathSum(root.right, remainder)
        return left or right

    # def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
    #     def dfs(node, curr):
    #         if not node:
    #             return False
    #         # if both children are null, then the node is a leaf
    #         if node.left is None and node.right is None:
    #             return (curr + node.val) == targetSum
    #         curr += node.val
    #         left = dfs(node.left, curr)
    #         right = dfs(node.right, curr)
    #         return left or right

    # Given the root of a binary tree, find the number of nodes that are good. A node is good if the path between the root
    # and the node has no nodes with a greater value.
    def goodNodes(self, root: Optional[TreeNode], maxSoFar: Optional[float] = float("-inf")) -> int:
        if not root:
            return 0
        good = 0
        if root.val >= maxSoFar:
            maxSoFar = root.val
            good = 1
        left = self.goodNodes(root.left, maxSoFar)
        right = self.goodNodes(root.right, maxSoFar)
        return left + right + good

    #     return dfs(root, 0)
    # def goodNodes(self, root: TreeNode) -> int:
    #     def dfs(node, max_so_far):
    #         if not node:
    #             return 0
    #         left = dfs(node.left, max(max_so_far, node.val))
    #         right = dfs(node.right, max(max_so_far, node.val))
    #         ans = left + right
    #         if node.val >= max_so_far:
    #             ans += 1
    #         return ans
    #     return dfs(root, float("-inf"))

    # Given the roots of two binary trees p and q, check if they are the same tree.
    # Two binary trees are the same tree if they are structurally identical and the nodes have the same values.

    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        if p is None and q is None:  # if there is no p node at the same time there is no q node, p & q are equal:
            return True
        if p is None or q is None:  # after the last if, either p & q both exist (skipping this if), or one exists (return False)
            return False
        if p.val != q.val:  # since both p & q exist, if their values are not equal:
            return False
        # if the previous 3 if statements did not return, the nodes from p & q exist and have matching values
        left = self.isSameTree(p.left, q.left)
        right = self.isSameTree(p.right, q.right)
        return left and right  # true when both left & right arrive at equal leaf nodes

    # Given the root of a binary tree and two nodes p and q that are in the tree, return the lowest common ancestor (LCA)
    #  of the two nodes. The LCA is the lowest node in the tree that has both p and q as descendants
    # (note: a node is a descendant of itself).

    def lowestCommonAncestor(self, root: "TreeNode", p: "TreeNode", q: "TreeNode") -> "TreeNode":
        if not root:
            return None
        if root.val == p or root.val == q:
            return root.val
        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)
        if left.val == p or left.val == q:
            return left.val
        if right.val == p or right.val == q:
            return right.val
        if left.val is not None and right.val is not None:
            return root.val


bs = BinarySearch()

eight = TreeNode(8)
seven = TreeNode(7)
four = TreeNode(4)
twelve = TreeNode(12, four)
three = TreeNode(3, twelve, seven)
five = TreeNode(5, eight, three)

eight1 = TreeNode(8)
seven1 = TreeNode(7)
four1 = TreeNode(4)
twelve1 = TreeNode(12, four1)
three1 = TreeNode(3, twelve1, seven1)
five1 = TreeNode(5, eight1, three1)

# print(bs.isSameTree(five, five1))  # returns True
print(bs.lowestCommonAncestor(five, four, seven))  # should return 3

# two = TreeNode(2)
# one = TreeNode(1, two)
# print(bs.hasPathSum(one, 1))  # return False
