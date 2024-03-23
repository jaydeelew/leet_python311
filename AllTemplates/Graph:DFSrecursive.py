# convert input graph into adjacency list or dictionary for this template


# e.g. to build adjacency dictionary for list of edges:
# def build_graph(edges):
#     graph = defaultdict(list)
#     for x, y in edges:
#         graph[x].append(y)
#         graph[y].append(x)  # undirected version has this line
#     return graph


# def fn(graph):
#     def dfs(node):
#         ans = 0
#         # do some logic
#         for neighbor in graph[node]:
#             if neighbor not in seen:
#                 seen.add(neighbor)
#                 ans += dfs(neighbor)

#         return ans

#     seen = {START_NODE}
#     return dfs(START_NODE)

# find the max depth of graph


def max_depth(graph):
    def dfs(node):
        ans = 0

        for neighbor in graph[node]:
            if neighbor not in seen:
                seen.add(neighbor)
                # for each stack frame, find the max return value of all neighbors plus 1 for this node
                ans = max(ans, dfs(neighbor) + 1)

        return ans

    seen = {0}
    return dfs(0)


def max_sum_root_to_leaf(graph):
    def dfs(node):
        ans = 0

        for neighbor in graph[node]:
            if neighbor not in seen:
                seen.add(neighbor)
                ans = max(ans, dfs(neighbor) + neighbor)

        return ans

    seen = {0}
    return dfs(0)


# edges is an adjacency list

edges = [[2, 3], [3], [0], [0, 1]]
# Output: 2

# edges = [[1, 4, 8], [0, 2, 3, 5], [1], [1, 9], [0, 6, 7], [1], [4], [4], [0], [3]]
# Output: 3

# edges = [[]]
# Output: 0

print(max_depth(edges))
print(max_sum_root_to_leaf(edges))
