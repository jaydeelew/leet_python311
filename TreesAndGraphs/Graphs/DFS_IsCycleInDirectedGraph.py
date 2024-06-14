def is_cyclic(graph, start_node):
    def dfs(node):
        if node in recursion_stack:
            return True  # Cycle detected
        if node in seen:
            return False  # Node already processed and no cycle was found from here

        seen.add(node)
        recursion_stack.add(node)
        for neighbor in graph[node]:
            if dfs(neighbor):
                return True
        recursion_stack.remove(node)
        return False

    seen = set()
    recursion_stack = set()
    for node in graph:  # Check all nodes to handle disconnected graphs
        if node not in seen:
            if dfs(node):
                return True
    return False


# Example usage:
graph = {0: [1], 1: [2], 2: [0], 3: [4], 4: []}  # Graph with a cycle (0 -> 1 -> 2 -> 0)
print("Graph has a cycle:", is_cyclic(graph, 0))
