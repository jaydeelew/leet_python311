# Given a directed acyclic graph (in adjacency list form) and a starting node,
# return the maximum sum of the graph from starting node to a leaf.


def max_sum(adj_list, start_node):
    def dfs(node):
        seen.add(node)

        max_sum = 0

        for neighbor in adj_list[node]:
            if neighbor not in seen:
                max_sum = max(max_sum, dfs(neighbor))

        # return the maximum sum returned from all the neighbors plus the value of this node
        return max_sum + node

    seen = set()
    return dfs(start_node)


graph = {0: [1, 3], 1: [2], 2: [], 3: [4, 5], 4: [], 5: []}
start = 0
print(max_sum(graph, start))

graph2 = {0: [1], 1: [2, 3, 4], 2: [], 3: [], 4: [5], 5: []}
start2 = 0
print(max_sum(graph2, start2))

graph3 = {0: [1], 1: [2], 2: [3], 3: []}
start3 = 0
print(max_sum(graph3, start3))

graph4 = {0: []}
start4 = 0
print(max_sum(graph4, start4))
