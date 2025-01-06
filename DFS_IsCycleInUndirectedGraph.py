def is_cyclic(graph):
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


# Example usage:
graph = {0: [1, 2], 1: [0, 2], 2: [0, 1], 3: [4], 4: [3]}  # Graph with a cycle (0 <-> 1 <-> 2 <-> 0)
print("Graph has a cycle:", is_cyclic(graph))
