# 0. Detect Cycle Directed Graph
# Given a directed graph in the form of an adjacency list and a starting node,
# return True if the graph contains a cycle, otherwise False.


def detectCycle(graph):
    def dfs(node):
        if node in recursion_stack:
            return True  # Cycle detected.
        if node in seen:
            return False  # Node already processed and no cycle was found from here.

        seen.add(node)
        # recursion_stack tracks nodes in the currenct DFS path.
        recursion_stack.add(node)
        for neighbor in graph[node]:
            if dfs(neighbor):
                return True
        recursion_stack.remove(node)
        return False

    seen = set()
    recursion_stack = set()
    # Check all nodes to handle disconnected graphs.
    for node in graph:
        if node not in seen:
            if dfs(node):
                return True
    return False


graph = {0: [1], 1: [2], 2: [0], 3: [4], 4: []}  # Graph with a cycle (0 -> 1 -> 2 -> 0)
# graph = {0: [1, 2], 1: [2], 2: []}  # Graph without cycle.
print("Graph has a cycle:", detectCycle(graph))
