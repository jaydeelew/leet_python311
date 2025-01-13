# 1026. Maximum Difference Between Node and Ancestor
# Given the root of a binary tree, find the maximum value v for which there exist different nodes a and b
# where v = |a.val - b.val| and a is an ancestor of b.
# A node a is an ancestor of b if either: any child of a is equal to b or any child of a is an ancestor of b.
class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class BinaryDFS:
    def maxAncestorDiff(self, root: TreeNode) -> int:
        if not root:
            return 0
        # record the maximum difference from helper function in result
        self.result = 0

        # nested helper function needed to pass current max and min value and report result to parent function
        def helper(node, cur_max_val, cur_min_val):
            if not node:
                return
            # update current maximum difference in result
            self.result = max(self.result, abs(cur_max_val - node.val), abs(cur_min_val - node.val))
            # update the current max and min values
            cur_max_val = max(cur_max_val, node.val)
            cur_min_val = min(cur_min_val, node.val)
            # if left or right nodes exist, update the max of their absolute differences from cur_min and cur_max to self.result
            helper(node.left, cur_max_val, cur_min_val)
            helper(node.right, cur_max_val, cur_min_val)

        # call helper with root node and current max & min vals (which are intitially the same)
        helper(root, root.val, root.val)
        return self.result


dfs = BinaryDFS()

nine = TreeNode(9)
seven = TreeNode(7)
four = TreeNode(4)
eight = TreeNode(8, nine)
twelve = TreeNode(12, four)
three = TreeNode(3, twelve, seven)
five = TreeNode(5, eight, three)  # root node

print(dfs.maxAncestorDiff(five))  # Output: 9
