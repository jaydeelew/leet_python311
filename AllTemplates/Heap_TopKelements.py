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


# find top k elements in arr
import heapq


def top_k(arr, k):
    min_heap = []

    for n in arr:
        if len(min_heap) < k:
            heapq.heappush(min_heap, n)
        else:
            heapq.heappushpop(min_heap, n)

    min_heap.sort(reverse=True)
    return min_heap


arr = [3, 6, 7, 2, 9, 4]
k = 3

print(top_k(arr, k))
# Output: 9, 7, 6
