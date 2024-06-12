import heapq


def dijkstra(adj_list, starting_node):
    # distances maintains the shortest distance from the starting node to all other vertices
    distances = dict.fromkeys(adj_list, float("inf"))
    # distances = {node: float('inf') for node in adj_list}
    distances[starting_node] = 0
    # list of tuples: (current minimum distance from start, current node)
    min_heap = [(0, starting_node)]
    # seen is needed to prevent revisiting nodes that already have their shortest distance from start computed
    seen = set()

    while min_heap:
        # we use a min heap here to potentially reduce the number of times we update the distance of a node
        # a FIFO queue could allow greater distances to be updated in distances first
        # whereas if a shorter distance is added first, greater distances will be ignored
        dist_from_start, node = heapq.heappop(min_heap)

        if node not in seen:
            # a seen neighbor's distance from start can still
            # be updated in distances by the current node
            seen.add(node)

            # for each neighbor of the current node, we calculate the distance from start to neighbor
            for neighbor, dist_to_neighbor in adj_list[node].items():
                dist_start_to_neighbor = dist_from_start + dist_to_neighbor

                # if the distance from start neighbor is shorter than the total distance recorded thus far,
                # we update the distance in distances and push the neighbor onto the heap
                if dist_start_to_neighbor < distances[neighbor]:
                    distances[neighbor] = dist_start_to_neighbor
                    heapq.heappush(min_heap, (dist_start_to_neighbor, neighbor))

    return distances


# adj_list = {
#     "A": {"B": 1, "C": 4},
#     "B": {"A": 1, "C": 2, "D": 5},
#     "C": {"A": 4, "B": 2, "D": 1},
#     "D": {"B": 5, "C": 1},
# }

# print(dijkstra(adj_list, "A"))
# Output: {'A': 0, 'B': 1, 'C': 3, 'D': 4}

adj_list = {
    "S": {"A": 8, "B": 4},
    "A": {"B": 4},
    "B": {"A": 3, "C": 2, "D": 5},
    "C": {"D": 2},
    "D": {},
}

print(dijkstra(adj_list, "S"))
# Output: {'S': 0, 'A': 7, 'B': 4, 'C': 6, 'D': 8}
