# 0. Sum All Nodes of a Graph
# Given a graph in adjacency list form, return the sum of all nodes.


def sumAllNodes(graph):
    # no stack or queue needed since we don't care about the order we visit the nodes
    seen = set()
    total = 0

    # Process each node only once
    for node in graph:
        if node not in seen:
            seen.add(node)
            total += node
            # Only process neighbors if we haven't seen them before
            for neighbor in graph[node]:
                if neighbor not in seen:
                    seen.add(neighbor)
                    total += neighbor

    return total


# Test cases
def test_sumAllNodes():
    # Test 1: Original test case
    graph1 = {0: [1, 2], 1: [0, 2, 3], 2: [0, 1], 3: [1]}
    assert sumAllNodes(graph1) == 6, "Test 1 failed"

    # Test 2: Single node graph
    graph2 = {0: []}
    assert sumAllNodes(graph2) == 0, "Test 2 failed"

    # Test 3: Disconnected components
    graph3 = {0: [1], 1: [0], 2: [3], 3: [2]}
    assert sumAllNodes(graph3) == 6, "Test 3 failed"

    # Test 4: Cycle
    graph4 = {0: [1], 1: [2], 2: [3], 3: [0]}
    assert sumAllNodes(graph4) == 6, "Test 4 failed"

    # Test 5: Larger numbers
    graph5 = {10: [20], 20: [30], 30: [10]}
    assert sumAllNodes(graph5) == 60, "Test 5 failed"

    print("All tests passed!")


# Run tests
test_sumAllNodes()
