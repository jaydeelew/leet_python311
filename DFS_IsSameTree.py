# 100. Given the roots of two binary trees p and q, check if they are the same tree.
# Two binary trees are the same tree if they are structurally identical and the nodes have the same values.
class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class BinaryDFS:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        # if there is no p node at the same time there is no q node, p & q are equal:
        if p is None and q is None:
            return True
        # after the last if, either p & q both exist (skipping this if), or one exists (return False)
        if p is None or q is None:
            return False
        # since both p & q exist, if their values are not equal:
        if p.val != q.val:
            return False
        # if the previous 3 if statements did not return, the nodes from p & q exist and have matching values
        left = self.isSameTree(p.left, q.left)
        right = self.isSameTree(p.right, q.right)
        # true when both left & right arrive at equal leaf nodes
        return left and right


dfs = BinaryDFS()

nine = TreeNode(9)
seven = TreeNode(7)
four = TreeNode(4)
eight = TreeNode(8, nine)
twelve = TreeNode(12, four)
three = TreeNode(3, twelve, seven)
five = TreeNode(5, eight, three)  # root node

nine1 = TreeNode(9)
seven1 = TreeNode(7)
four1 = TreeNode(4)
eight1 = TreeNode(8, nine1)
twelve1 = TreeNode(12, four1)
three1 = TreeNode(3, twelve1, seven1)
five1 = TreeNode(5, eight1, three1)  # root node

print(dfs.isSameTree(five, five1))  # Output: True
