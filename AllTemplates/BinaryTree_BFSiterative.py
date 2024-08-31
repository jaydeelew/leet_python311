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


def bfs_iterative(root):
    # [root], and not "root" alone, is necessary since deque requires an iterable
    queue = deque([root])
    ans = []

    while queue:
        # do some logic here for the current level:
        # e.g.:
        current_level_values = [node.val for node in queue]
        ans.append(current_level_values)

        num_of_nodes_curr_level = len(queue)

        for _ in range(num_of_nodes_curr_level):
            node = queue.popleft()
            # do some logic here for current node
            # e.g.:
            # print(node.val, end=" ")

            # putting next level onto the queue with completion of for loop
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

print(bfs_iterative(five))  # Output: [[5], [8, 3], [9, 12, 7], [4]]
print()  # new line
