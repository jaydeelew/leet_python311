# 0. Merge Sorted Arrays
# Given two sorted integer arrays, return a new sorted array that combines both of them and is also sorted.


def merge_sorted_arrays(arr1, arr2):
    return sorted(arr1 + arr2)

    # Time Complexity: O(n log n), where n is the total number of elements in both arrays.
    # This is because the sorted() function uses the Timsort algorithm, which has a time complexity of O(n log n).
    #
    # Space Complexity: O(n), where n is the total number of elements in both arrays.
    # This is because the sorted() function creates a new sorted array to store the combined elements.


def merge_sorted_arrays_2(arr1, arr2):
    merged = []
    i = j = 0
    while i < len(arr1) and j < len(arr2):
        if arr1[i] <= arr2[j]:
            merged.append(arr1[i])
            i += 1
        else:
            merged.append(arr2[j])
            j += 1

    while i < len(arr1):
        merged.append(arr1[i])
        i += 1

    while j < len(arr2):
        merged.append(arr2[j])
        j += 1

    # Or more simply:
    # merged.extend(arr1[i:])
    # merged.extend(arr2[j:])

    return merged

    # Time Complexity: O(n + m), where n and m are the lengths of arr1 and arr2 respectively.
    # This is because we iterate through each element of both arrays once.
    #
    # Space Complexity: O(n + m), as we create a new merged array to store the combined sorted elements.


arr1 = [1, 4, 7, 20]
arr2 = [3, 5, 6]
# Output: [1, 3, 4, 5, 6, 7, 20]

print(merge_sorted_arrays(arr1, arr2))
print(merge_sorted_arrays_2(arr1, arr2))
