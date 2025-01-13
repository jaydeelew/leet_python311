# 0. Max Depth DAG
# Given a directed acyclic graph (in adjacency list form) and a starting node,
# return the maximum depth of the graph from starting node to a leaf.


def maxDepth(adj_list, node):
    max_depth = 0

    for neighbor in adj_list[node]:
        # The plus one counts the edge to the neighbor.
        # Since a leaf node has no neighbors, it will return 0 edges.
        max_depth = max(max_depth, maxDepth(adj_list, neighbor) + 1)

    return max_depth


# def maxDepth(adj_list, node):
#     # if tree node
#     if not adj_list[node]:
#         return 0
#     return 1 + max(maxDepth(adj_list, neighbor) for neighbor in adj_list[node])


graph1 = {0: [1, 3], 1: [2], 2: [], 3: [4, 5], 4: [], 5: []}
start1 = 0
print(maxDepth(graph1, start1))
# Output: 2

graph2 = {0: [1], 1: [2, 3, 4], 2: [], 3: [], 4: [5], 5: []}
start2 = 0
print(maxDepth(graph2, start2))
# Output: 3

graph3 = {0: [1], 1: [2], 2: [3], 3: []}
start3 = 0
print(maxDepth(graph3, start3))
# Output: 3

graph4 = {0: []}
start4 = 0
print(maxDepth(graph4, start4))
# Output: 0
