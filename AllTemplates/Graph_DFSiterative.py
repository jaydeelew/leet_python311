# build adjacency dictionary from list of edges:
# def build_graph(edges):
#     graph = defaultdict(list)
#     for x, y in edges:
#         graph[x].append(y)
#         graph[y].append(x)  # undirected version has this line
#     return graph


# def fn(graph):
#     stack = [START_NODE]
#     seen = {START_NODE}
#     ans = 0

#     while stack:
#         node = stack.pop()
#         # do some logic
#         for neighbor in graph[node]:
#             if neighbor not in seen:
#                 seen.add(neighbor)
#                 stack.append(neighbor)

#     return ans


def sum_nodes(adj_list):
    stack = [0]
    seen = {0}
    ans = 0

    while stack:
        node = stack.pop()
        ans += node

        for neighbor in adj_list[node]:
            if neighbor not in seen:
                seen.add(neighbor)
                stack.append(neighbor)

    return ans


graph = {0: [2, 1], 1: [3], 2: [1], 3: []}
# Output: 6

print(sum_nodes(graph))
