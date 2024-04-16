# import heapq

# distances = [inf] * n
# distances[source] = 0
# heap = [(0, source)]

# while heap:
#     curr_dist, node = heappop(heap)
#     if curr_dist > distances[node]:
#         continue

#     for nei, weight in graph[node]:
#         dist = curr_dist + weight
#         if dist < distances[nei]:
#             distances[nei] = dist
#             heappush(heap, (dist, nei))

import heapq


def calculate_distances(graph, starting_vertex):
    distances = {vertex: float("inf") for vertex in graph}
    distances[starting_vertex] = 0

    # (current distance, current vertex)
    pq = [(0, starting_vertex)]

    while pq:
        current_distance, current_vertex = heapq.heappop(pq)

        # Nodes can get added to the priority queue multiple times. We only
        # process a vertex the first time we remove it from the priority queue.
        if current_distance > distances[current_vertex]:
            continue

        for neighbor, weight in graph[current_vertex].items():
            distance = current_distance + weight

            # Only consider this new path if it's better than any path we've
            # already found.
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(pq, (distance, neighbor))

    return distances


example_graph = {
    "U": {"V": 2, "W": 5, "X": 1},
    "V": {"U": 2, "X": 2, "W": 3},
    "W": {"V": 3, "U": 5, "X": 3, "Y": 1, "Z": 5},
    "X": {"U": 1, "V": 2, "W": 3, "Y": 1},
    "Y": {"X": 1, "W": 1, "Z": 1},
    "Z": {"W": 5, "Y": 1},
}

print(calculate_distances(example_graph, "U"))
