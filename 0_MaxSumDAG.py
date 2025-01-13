# 0. Max Sum DAG
# Given a directed acyclic graph (in adjacency list form) and a starting node,
# return the maximum sum of the graph from starting node to a leaf.


def maxSum(adj_list, node):
    max_sum = 0

    for neighbor in adj_list[node]:
        max_sum = max(max_sum, maxSum(adj_list, neighbor))

    return max_sum + node


# def maxSum(adj_list, node):
#     if node not in adj_list:
#         return 0
#     # if leaf node (empty neighbors list)
#     if not adj_list[node]:
#         return node
#     return node + max(maxSum(adj_list, neighbor) for neighbor in adj_list[node])


graph = {0: [1, 3], 1: [2], 2: [], 3: [4, 5], 4: [], 5: []}
start = 0
print(maxSum(graph, start))
# Output: 8

graph2 = {0: [1], 1: [2, 3, 4], 2: [], 3: [], 4: [5], 5: []}
start2 = 0
print(maxSum(graph2, start2))
# Output: 10

graph3 = {0: [1], 1: [2], 2: [3], 3: []}
start3 = 0
print(maxSum(graph3, start3))
# Output: 6

graph4 = {0: []}
start4 = 0
print(maxSum(graph4, start4))
# Output: 0
