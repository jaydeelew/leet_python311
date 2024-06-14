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


def find_top_k_by_target_difference(arr, k, target):
    heap = []
    for num in arr:
        # negate the absolute difference to make it a max heap
        difference = -abs(num - target)
        heapq.heappush(heap, (difference, num))
        if len(heap) > k:
            heapq.heappop(heap)

    # sort heap list in descending order of the negated absolute difference
    # so that top k elements in arr are the closest to target
    heap.sort(reverse=True)
    return [num for _, num in heap]


def top_k(arr, k):  # O(nlog(k))
    heap = []
    for num in arr:  # O(n)
        heapq.heappush(heap, num)  # O(log(k))
        if len(heap) > k:
            heapq.heappop(heap)  # O(log(k))

    heap.sort()  # O(klog(k))
    return heap


def find_kth_largest(arr: list[int], k: int) -> int:  # O(nlog(n))
    heapq.heapify(arr)  # O(n)
    while len(arr) > k:  # O(n-k)
        heapq.heappop(arr)  # O(log(n))
    return arr[0]


arr = [3, 6, 7, 2, 9, 4]
k = 3
target = 1

print(find_top_k_by_target_difference(arr, k, target))
# Output: 2, 3, 4

print(top_k(arr, k))
# Output: 6, 7, 9

print(find_kth_largest(arr, k))
# Output: 6
