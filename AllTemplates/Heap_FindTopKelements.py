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


# find top k elements in arr
def top_k(arr, k):  # O(nlog(k))
    heap = []
    for num in arr:  # O(n)
        heapq.heappush(heap, num)  # O(log(k))
        if len(heap) > k:
            heapq.heappop(heap)  # O(log(k))

    heap.sort()  # O(klog(k))
    return heap


# find kth largest element in arr
def find_kth_largest(arr: list[int], k: int) -> int:  # O(nlog(n))
    heapq.heapify(arr)  # O(n)
    while len(arr) > k:  # O(n-k)
        heapq.heappop(arr)  # O(log(n))
    return arr[0]


arr = [3, 6, 7, 2, 9, 4]
k = 3

print(top_k(arr, k))
# Output: 6, 7, 9

print(find_kth_largest(arr, k))
# Output: 6
