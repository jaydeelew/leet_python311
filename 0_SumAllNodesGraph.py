# 0. Sum All Nodes of a Graph
# Given a graph in adjacency list form, return the sum of all nodes.


def sumAllNodesIterative(adj_list):
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


def sumAllNodesRecursive(adj_list):

    def dfs(node):
        # the base case occurs when there are no more neighbors
        # i.e. 0 will be returned
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

print(sumAllNodesIterative(graph))
print(sumAllNodesRecursive(graph))
