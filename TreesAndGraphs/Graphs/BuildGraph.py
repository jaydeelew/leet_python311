from collections import defaultdict

# build graphs in the form of a dictionary for the following 2D-array graph-input formats:
# array of edges
# adjacency list
# adjacency matrix
# *all forms above in both directed and undirected graphs


def build_undirected_graph_1(edges):
    graph = defaultdict(list)
    for x, y in edges:
        graph[x].append(y)
        graph[y].append(x)  # undirected version has this line
    return graph


def build_directed_graph_1(edges):
    graph = defaultdict(list)
    for x, y in edges:
        graph[x].append(y)
    return graph


def build_graph_2(adj_list):
    graph = defaultdict(list)
    for i in range(len(adj_list)):
        if adj_list[i]:
            for node in adj_list[i]:
                graph[i].append(node)
    return graph


def build_undirected_graph_3(adj_matrix):
    n = len(adj_matrix)
    graph = defaultdict(list)  # defaultdict allows us to append values to keys that do not yet exist. They will be created.
    for i in range(n):
        for j in range(i + 1, n):  # main diagonal and values below it are ignored
            if adj_matrix[i][j]:  # if result is 1
                graph[i].append(j)  # above main diagonal
                graph[j].append(i)  # below main diagonal (since undirected graph includes mirror entry)
    return graph


def build_directed_graph_3(adj_matrix):
    n = len(adj_matrix)
    graph = defaultdict(list)  # defaultdict allows us to append values to keys that do not yet exist. They will be created.
    for i in range(n):
        for j in range(n):
            if adj_matrix[i][j]:  # if result is 1
                graph[i].append(j)  # above main diagonal
    return graph


# directed version
# 0 -> 1 -> 2 -> 3
# ^         |
# |_________|

# undirected version
#     0
#   /   \
#  1 --- 2 --- 3

# array of edges
edges = [[0, 1], [1, 2], [2, 0], [2, 3]]
# adjacency list
adj_list_directed = [[1], [2], [0, 3], []]
adj_list_undirected = [[1, 2], [0, 2], [0, 1, 3], [2]]
# adjacency matrix
adj_matrix_directed = [[0, 1, 0, 0], [0, 0, 1, 0], [1, 0, 0, 1], [0, 0, 0, 0]]
adj_matrix_undirected = [[0, 1, 1, 0], [1, 0, 1, 0], [1, 1, 0, 1], [0, 0, 1, 0]]

print(build_directed_graph_1(edges))
print(build_graph_2(adj_list_directed))
print(build_directed_graph_3(adj_matrix_directed))
print("")
print(build_undirected_graph_1(edges))
print(build_graph_2(adj_list_undirected))
print(build_undirected_graph_3(adj_matrix_undirected))
