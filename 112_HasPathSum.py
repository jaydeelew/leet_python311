# 112. Path Sum
# Given the root of a binary tree and an integer targetSum,
# return true if the tree has a root-to-leaf path such that adding up all the values along the path equals targetSum.


def hasPathSum(root, targetSum):
    if not root:
        return False

    if not root.left and not root.right:  # leaf node
        # After reducing targetSum by each node.val,
        # do we arrive at a leaf value that equals the remainder of targetSum?
        return root.val == targetSum

    # If either of these return True, we have a final True return at the bottom of the stack.
    return hasPathSum(root.left, targetSum - root.val) or hasPathSum(root.right, targetSum - root.val)


class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


one = TreeNode(1)
seven = TreeNode(7)
two = TreeNode(2)
thirteen = TreeNode(13)
eleven = TreeNode(11, seven, two)
four_a = TreeNode(4, eleven)
four_b = TreeNode(4, right=one)
eight = TreeNode(8, thirteen, four_b)
five = TreeNode(5, four_a, eight)  # root node

targetSum = 22
# Output: True

print(hasPathSum(five, targetSum))
