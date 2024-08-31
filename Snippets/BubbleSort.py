def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        # For each iteration, compare adjacent elements
        for j in range(0, n - i - 1):
            # If the element found is greater than the next element, swap them
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr


test_array = [64, 34, 25, 12, 22, 11, 90]
print("Original array:", test_array)
sorted_array = bubble_sort(test_array)
print("Sorted array:", sorted_array)
