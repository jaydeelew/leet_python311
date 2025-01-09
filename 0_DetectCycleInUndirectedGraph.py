# 0. Detect Cycle Undirected Graph
# Given an undirected graph in the form of an adjacency list and a starting node,
# return True if the graph contains a cycle, otherwise False.


def detectCycle(graph):
    def dfs(node, parent):
        seen.add(node)
        for neighbor in graph[node]:
            if neighbor not in seen:
                if dfs(neighbor, node):
                    return True
            elif parent != neighbor:
                return True
        return False

    seen = set()
    for node in graph:
        if node not in seen:
            if dfs(node, None):
                return True
    return False


graph = {0: [1, 2], 1: [0, 2], 2: [0, 1], 3: [4], 4: [3]}  # Graph with a cycle (0 <-> 1 <-> 2 <-> 0)
# graph = {0: [1, 2], 1: [0], 2: [0], 3: [4], 4: [3]}  # Graph without a cycle (0 <-> 1 <-> 2 <-> 3)
print("Graph has a cycle:", detectCycle(graph))
