# build adjacency dictionary from list of edges:
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


def sum_nodes(adj_list):

    def dfs(node):
        # the base case occurs when there are no more neighbors
        ans = 0

        for neighbor in graph[node]:
            if neighbor not in seen:
                seen.add(neighbor)
                ans += dfs(neighbor) + neighbor

        return ans

    seen = {0}
    return dfs(0)


graph = {0: [2, 1], 1: [3], 2: [1], 3: []}
# Output: 6

print(sum_nodes(graph))
