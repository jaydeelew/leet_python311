def insertion_sort(arr):
    for i in range(1, len(arr)):
        # Store the current element as the key to be inserted
        key = arr[i]
        # Start from the element before the key
        j = i - 1
        # While there are elements in the sorted portion that are greater than the key
        while j >= 0 and arr[j] > key:
            # Shift the element to the right
            arr[j + 1] = arr[j]
            # Move to the next element
            j -= 1
        # Insert the key in its correct position
        arr[j + 1] = key
    return arr


test_array = [64, 34, 25, 12, 22, 11, 90]
print("Original array:", test_array)
sorted_array = insertion_sort(test_array)
print("Sorted array:", sorted_array)
