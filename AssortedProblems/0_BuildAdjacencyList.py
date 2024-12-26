# 0. Build Adjacency List
# Build an undirected adjacency list from list of edges.
from collections import defaultdict


def buildAdjList(edges):
    adj_list = defaultdict(list)

    for e in edges:
        adj_list[e[0]].append(e[1])
        # Without this line we have a directed adjacency list
        adj_list[e[1]].append(e[0])

    return adj_list


edges = [(0, 1), (0, 3), (1, 3), (2, 3), (3, 5)]
# Output = {0: [1, 3], 1: [0, 3], 3: [0, 1, 2, 5], 2: [3], 5: [3]}

print(buildAdjList(edges))
