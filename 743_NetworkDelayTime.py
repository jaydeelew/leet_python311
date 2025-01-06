# 743. Network Delay Time
# You are given a network of n nodes, labeled from 1 to n.
# You are also given times, a list of travel times as directed edges times[i] = (ui, vi, wi),
# where ui is the source node, vi is the target node,
# and wi is the time it takes for a signal to travel from source to target.
# We will send a signal from a given node k.
# Return the minimum time it takes for all the n nodes to receive the signal.
# If it is impossible for all the n nodes to receive the signal, return -1.
import heapq
from collections import defaultdict


def networkDelayTime(times, n, k):
    distances = {node: float("inf") for node in range(1, n + 1)}
    distances[k] = 0
    min_heap = [(0, k)]
    seen = set()

    adj_list = defaultdict(list)
    for source, target, time in times:
        adj_list[source].append((target, time))

    while min_heap:
        dist_from_k, node = heapq.heappop(min_heap)

        if node not in seen:
            seen.add(node)

            for target, dist_to_target in adj_list[node]:
                dist_from_k_to_target = dist_from_k + dist_to_target
                if dist_from_k_to_target < distances[target]:
                    distances[target] = dist_from_k_to_target
                    heapq.heappush(min_heap, (dist_from_k_to_target, target))

    if any(val == float("inf") for val in distances.values()):
        return -1

    return max(distances.values())


times = [[2, 1, 1], [2, 3, 1], [3, 4, 1]]
n = 4
k = 2
# Output: 2

# times = [[1, 2, 1]]
# n = 2
# k = 1
# Output: 1

# times = [[1, 2, 1]]
# n = 2
# k = 2
# Output: -1

print(networkDelayTime(times, n, k))
