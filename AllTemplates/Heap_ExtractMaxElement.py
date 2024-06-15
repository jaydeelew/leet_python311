import heapq


def extract_max_element(arr):
    # Convert the list into a max heap by inverting the values
    max_heap = [-x for x in arr]
    heapq.heapify(max_heap)

    # Extract the maximum element and negate it to get the original value
    max_element = -heapq.heappop(max_heap)
    return max_element


test_array = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]  # Output: 9
print(extract_max_element(test_array))
