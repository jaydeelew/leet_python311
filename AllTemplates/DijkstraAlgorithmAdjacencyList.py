import heapq


def dijkstra(graph, starting_node):
    # distances maintains the shortest distance from the starting node to all other vertices
    total_distances = dict.fromkeys(graph, float("inf"))
    total_distances[starting_node] = 0

    # list of tuples: (current minimum distance from start, current node)
    min_heap = [(0, starting_node)]
    seen = set()

    while min_heap:
        # we use a min heap here to potentially reduce the number of times we update the distance of a node
        # a FIFO queue could allow greater distances to be updated in total_distances first
        # whereas if a shorter distance is added first, greater distances will be ignored
        curr_node_dist_from_start, current_node = heapq.heappop(min_heap)

        if current_node in seen:
            continue
        # a seen neighbor's distance from start can still
        # be updated in total_distances by the current node
        seen.add(current_node)

        # for each neighbor of the current node, we calculate the distance from start to neighbor
        for neighbor, dist_curr_node_to_neighbor in graph[current_node].items():
            dist_start_to_neighbor = curr_node_dist_from_start + dist_curr_node_to_neighbor

            # if the distance from start neighbor is shorter than the total distance recorded thus far,
            # we update the distance in total_distances and push the neighbor onto the heap
            if dist_start_to_neighbor < total_distances[neighbor]:
                total_distances[neighbor] = dist_start_to_neighbor
                heapq.heappush(min_heap, (dist_start_to_neighbor, neighbor))

    return total_distances


# graph = {
#     "A": {"B": 1, "C": 4},
#     "B": {"A": 1, "C": 2, "D": 5},
#     "C": {"A": 4, "B": 2, "D": 1},
#     "D": {"B": 5, "C": 1},
# }

# print(dijkstra(graph, "A"))
# Output: {'A': 0, 'B': 1, 'C': 3, 'D': 4}

graph = {
    "S": {"A": 8, "B": 4},
    "A": {"B": 4},
    "B": {"A": 3, "C": 2, "D": 5},
    "C": {"D": 2},
    "D": {},
}

print(dijkstra(graph, "S"))
# Output: {'S': 0, 'A': 7, 'B': 4, 'C': 6, 'D': 8}
