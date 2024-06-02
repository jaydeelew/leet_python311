# import heapq

# def fn(arr, k):
#     heap = []
#     for num in arr:
#       # do some logic to push onto heap according to problem's criteria
# i.e. heap is ordered by CRITERIA, this first item of the tuple if tuple is used
#         heapq.heappush(heap, (CRITERIA, num))
#         if len(heap) > k:
#             heapq.heappop(heap)

#     return [num for num in heap]

import heapq


def top_k(arr, k):
    heap = []
    for num in arr:
        heapq.heappush(heap, num)
        if len(heap) > k:
            heapq.heappop(heap)

    return sorted([num for num in heap])


def find_kth_largest(arr: list[int], k: int) -> int:
    heapq.heapify(arr)
    while len(arr) > k:
        heapq.heappop(arr)
    return arr[0]


arr = [3, 6, 7, 2, 9, 4]
k = 3

print(top_k(arr, k))
# Output: 6, 7, 9

print(find_kth_largest(arr, k))
# Output: 6
