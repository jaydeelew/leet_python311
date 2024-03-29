# from collections import deque

# def fn(root):
#     queue = deque([root])
#     ans = 0

#     while queue:
#         current_length = len(queue)
#         # do logic for current level

#         for _ in range(current_length):
#             node = queue.popleft()
#             # do logic
#             if node.left:
#                 queue.append(node.left)
#             if node.right:
#                 queue.append(node.right)

#     return ans


from collections import deque


class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def print_all_nodes(root):
    # [root], and not "root" alone, is necessary since deque requires an iterable
    queue = deque([root])
    ans = []
    while queue:
        nodes_in_current_level = len(queue)
        # do some logic here for the current level if needed

        for _ in range(nodes_in_current_level):
            node = queue.popleft()
            # do some logic here on the current node
            ans.append(node.val)

            # put the next level onto the queue
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
    return ans


nine = TreeNode(9)
seven = TreeNode(7)
four = TreeNode(4)
eight = TreeNode(8, nine)
twelve = TreeNode(12, four)
three = TreeNode(3, twelve, seven)
five = TreeNode(5, eight, three)  # root node

print(print_all_nodes(five))  # Output: 5 8 3 9 12 7 4
