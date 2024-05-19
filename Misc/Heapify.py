from heapq import heappush, heappop, heapify


# make a heap from an array in place
def make_heap(arr):
    heapify(arr)
    return arr


def heap_push(heap, element):
    heappush(heap, element)
    return heap


def heap_pop(heap):
    return heappop(heap)


def print_heap(heap):
    print(heap)


test_array = [5, 3, 8, 6, 2, 9, 1, 7, 4, 0]

print(f"{test_array} - Array before heapify")
make_heap(test_array)
print(f"{test_array} - Array after heapify")

while test_array:
    print(heap_pop(test_array), end=" ")

print(f"{test_array} - Array after heap pops")
