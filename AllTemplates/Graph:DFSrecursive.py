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
def max_depth(adj_list):
    def dfs(node):
        ans = 0

        for neighbor in adj_list[node]:
            if neighbor not in seen:
                seen.add(neighbor)
                # max depth of previous max vs. neighbor plus 1 for this node
                ans = max(ans, dfs(neighbor) + 1)

        return ans

    # seen must be outside of dfs since placing it inside would reset it to {0} every time
    seen = {0}
    return dfs(0)


def max_sum_root_to_leaf(adj_list):
    def dfs(node):
        ans = 0

        for neighbor in adj_list[node]:
            if neighbor not in seen:
                seen.add(neighbor)
                ans = max(ans, dfs(neighbor) + neighbor)

        return ans

    seen = {0}
    return dfs(0)


edges = {0: [2, 3], 1: [3], 2: [0], 3: [0, 1]}
# max_depth output: 2
# max_sum_root_to_leaf output: 4

# edges = {0: [1, 4, 8], 1: [0, 2, 3, 5], 2: [1], 3: [1, 9], 4: [0, 6, 7], 5: [1], 6: [4], 7: [4], 8: [0], 9: [3]}
# max_depth output: 3
# max_sum_root_to_leaf output: 13

# edges = {0: []}
# max_depth output: 0
# max_sum_root_to_leaf output: 0

print(max_depth(edges))
print(max_sum_root_to_leaf(edges))
