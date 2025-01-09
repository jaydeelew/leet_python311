# 0. Build Adjacency Lists
# Build an undirected adjacency list from list of edges.
from collections import defaultdict


def buildAdjListDirectedEdges(edges):
    adj_list = defaultdict(list)

    for e in edges:
        adj_list[e[0]].append(e[1])
        if e[1] not in adj_list:
            # defaultdict creates a key with an empty list
            adj_list[e[1]]

    return dict(adj_list)


def buildAdjListUndirectedEdges(edges):
    adj_list = defaultdict(list)

    for e in edges:
        adj_list[e[0]].append(e[1])
        adj_list[e[1]].append(e[0])

    return dict(adj_list)


def buildAdjListDirectedMatrix(adj_matrix):
    n = len(adj_matrix)
    # defaultdict allows us to append values to keys that do not yet exist. They will be created.
    adj_list = defaultdict(list)
    for i in range(n):
        for j in range(i + 1, n):  # main diagonal and values below it are ignored
            if adj_matrix[i][j]:  # if result is 1
                adj_list[i].append(j)  # above main diagonal
                adj_list[j].append(i)  # below main diagonal (since undirected adj_list includes mirror entry)
    return dict(adj_list)


def buildAdjListUndirectedMatrix(adj_matrix):
    n = len(adj_matrix)
    # defaultdict allows us to append values to keys that do not yet exist. They will be created.
    adj_list = defaultdict(list)
    for i in range(n):
        for j in range(n):
            if adj_matrix[i][j]:  # if result is 1
                adj_list[i].append(j)  # above main diagonal
    return dict(adj_list)


edges = [(0, 1), (0, 3), (1, 3), (3, 2), (3, 5)]
# Output Directed Edges: {0: [1, 3], 1:[3], 2:[], 3:[2, 5], 5:[]}
# Output Undirected Edges: {0: [1, 3], 1: [0, 3], 3: [0, 1, 2, 5], 2: [3], 5: [3]}
adj_matrix_directed = [[0, 1, 0, 0], [0, 0, 1, 0], [1, 0, 0, 1], [0, 0, 0, 0]]
# Output Directed Matrix: {0: [1], 1: [0, 2], 2: [1, 3], 3: [2]}
adj_matrix_undirected = [[0, 1, 1, 0], [1, 0, 1, 0], [1, 1, 0, 1], [0, 0, 1, 0]]
# Output Undirected Matrix: {0: [1, 2], 1: [0, 2], 2: [0, 1, 3], 3: [2]}

print(buildAdjListDirectedEdges(edges))
print(buildAdjListUndirectedEdges(edges))
print(buildAdjListDirectedMatrix(adj_matrix_directed))
print(buildAdjListUndirectedMatrix(adj_matrix_undirected))
