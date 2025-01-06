# 0. Minimum Depth to Leaf
# Given a graph in the form of an adjacency list and a starting node,
# find the minimum depth to a leaf node.
# The function should work for directed and undirected graphs.
# It should return -1 if the graph contains no leaf nodes.

from collections import deque


def minDepthToLeaf(adj_list, start_node):

    # if start_node is not in the list or there are no nodes
    if start_node not in adj_list or not adj_list:
        return -1

    # if start_node is a leaf (has no children)
    if not adj_list[start_node]:
        return 0

    q = deque([start_node])
    seen = {start_node}
    depth = 0
    directed_graph = False

    if len(adj_list[start_node]) > 0:
        first_neighbor = adj_list[start_node][0]
        if start_node not in adj_list[first_neighbor]:
            directed_graph = True

    while q:
        depth += 1
        num_nodes_in_level = len(q)
        # it is necessary to record number of nodes currently in the queue
        # and not pass len(q) to the for loop, since len(q) changes each iteration
        for _ in range(num_nodes_in_level):
            node = q.popleft()
            for neighbor in adj_list[node]:
                if neighbor not in seen:
                    # if this is a directed graph and the list of neighbors is empty, there are no children,
                    # and we arrived at a leaf. Or,
                    # if this is an undirected graph, and there is only one neighbor in the list of neighbors,
                    # this one neighbor is the parent, and we arrived at a leaf.
                    if (directed_graph and not adj_list[neighbor]) or (not directed_graph and len(adj_list[neighbor]) == 1):
                        return depth
                    seen.add(neighbor)
                    q.append(neighbor)
    # if there are no leaves (such as in a cycle)
    return -1


directed = {
    0: [1, 4, 8],
    1: [2, 3, 5],
    2: [11],
    3: [9],
    4: [6, 7],
    5: [12],
    6: [],
    7: [],
    8: [10],
    9: [],
    10: [],
    11: [],
    12: [],
}  # Output: 2

undirected = {
    0: [1, 4, 8],
    1: [0, 2, 3, 5],
    2: [1, 11],
    3: [1, 9],
    4: [0, 6, 7],
    5: [1, 12],
    6: [4],
    7: [4],
    8: [0, 10],
    9: [3],
    10: [8],
    11: [2],
    12: [5],
}  # Output: 2

only_start_node = {0: []}  # Output: 0
empty = {}  # Output: -1
cycle_directed = {0: [1], 1: [2], 2: [0]}  # Output: -1
cycle_undirected = {0: [1, 2], 1: [0, 2], 2: [0, 1]}  # Output: -1

print(minDepthToLeaf(directed, 0))
print(minDepthToLeaf(undirected, 0))
print(minDepthToLeaf(only_start_node, 0))
print(minDepthToLeaf(empty, 0))
print(minDepthToLeaf(cycle_directed, 0))
print(minDepthToLeaf(cycle_undirected, 0))
