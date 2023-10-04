from collections import deque


class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class BinaryBFS:
    def print_all_nodes(self, root):
        queue = deque([root])  # [root], and not "root" alone, is necessary since deque requires an iterable
        while queue:
            nodes_in_current_level = len(queue)
            # do some logic here for the current level

            for _ in range(nodes_in_current_level):
                node = queue.popleft()
                # do some logic here on the current node
                print(node.val, end=" ")

                # put the next level onto the queue
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
        return ""  # return "" necessary for not printing "None" at final stack return


bfs = BinaryBFS()

nine = TreeNode(9)
seven = TreeNode(7)
four = TreeNode(4)
eight = TreeNode(8, nine)
twelve = TreeNode(12, four)
three = TreeNode(3, twelve, seven)
five = TreeNode(5, eight, three)  # root node

print(bfs.print_all_nodes(five))
print("")
