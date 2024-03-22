# convert input graph into adjacency list or dictionary for this template


# # e.g. to build adjacency dictionary for list of edges
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
