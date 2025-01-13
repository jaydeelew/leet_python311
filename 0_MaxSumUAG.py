# 0. Max Sum to Leaf in a Graph
# Given a undirected acyclic graph (in adjacency list form) and a starting node,
# return the maximum sum of the graph from starting node to a leaf.


def maxSum(adj_list, start_node, parent=None):
    def dfs(node, parent):
        # max_sum starts at 0 for each call to dfs since below the max sum
        # of all neighbors will be evaluated and then added to the value of this node
        max_sum = 0

        for neighbor in adj_list[node]:
            if neighbor != parent:
                max_sum = max(max_sum, dfs(neighbor, node))

        # return the maximum sum returned from all the neighbors plus the value of this node
        return max_sum + node

    return dfs(start_node, parent)


# def maxSum(adj_list, node, parent=None):
#     # if root has no children
#     if not adj_list[node]:
#         return 0
#     # if leaf node
#     if len(adj_list[node]) == 1 and adj_list[node][0] == parent:
#         return node
#     return node + max(maxSum(adj_list, neighbor, node) for neighbor in adj_list[node] if neighbor != parent)


graph1 = {0: [1, 3], 1: [0, 2], 2: [1], 3: [0, 4, 5], 4: [3], 5: [3]}
start1 = 0
print(maxSum(graph1, start1))
# Output: 8

graph2 = {0: [1], 1: [0, 2, 3, 4], 2: [1], 3: [1], 4: [1, 5], 5: [4]}
start2 = 0
print(maxSum(graph2, start2))
# Output: 10

graph3 = {0: [1], 1: [0, 2], 2: [1, 3], 3: [2]}
start3 = 0
print(maxSum(graph3, start3))
# Output: 6

graph4 = {0: []}
start4 = 0
print(maxSum(graph4, start4))
# Output: 0
