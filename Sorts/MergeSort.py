def merge_sort(arr):
    # Base case: if array has 1 or fewer elements, it's already sorted
    if len(arr) <= 1:
        return arr

    # Find the middle point to divide array into two halves
    mid = len(arr) // 2

    # Recursively sort the two halves
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])

    # Merge the sorted halves
    return merge(left, right)


def merge(left, right):
    result = []
    left_idx, right_idx = 0, 0

    # Compare elements from both arrays and merge them in sorted order
    while left_idx < len(left) and right_idx < len(right):
        if left[left_idx] <= right[right_idx]:
            result.append(left[left_idx])
            left_idx += 1
        else:
            result.append(right[right_idx])
            right_idx += 1

    # Add remaining elements from left array, if any
    result.extend(left[left_idx:])
    # Add remaining elements from right array, if any
    result.extend(right[right_idx:])

    return result


# Test cases
def test_merge_sort():
    # Test case 1: Normal array
    arr1 = [64, 34, 25, 12, 22, 11, 90]
    print("Original array:", arr1)
    print("Sorted array:", merge_sort(arr1))

    # Test case 2: Array with duplicates
    arr2 = [5, 2, 8, 5, 1, 9, 2, 8]
    print("\nArray with duplicates:", arr2)
    print("Sorted array:", merge_sort(arr2))

    # Test case 3: Empty array
    arr3 = []
    print("\nEmpty array:", arr3)
    print("Sorted array:", merge_sort(arr3))

    # Test case 4: Single element array
    arr4 = [42]
    print("\nSingle element array:", arr4)
    print("Sorted array:", merge_sort(arr4))

    # Test case 5: Already sorted array
    arr5 = [1, 2, 3, 4, 5]
    print("\nAlready sorted array:", arr5)
    print("Sorted array:", merge_sort(arr5))

    # Test case 6: Reverse sorted array
    arr6 = [5, 4, 3, 2, 1]
    print("\nReverse sorted array:", arr6)
    print("Sorted array:", merge_sort(arr6))

    # Test case 7: Array with negative numbers
    arr7 = [-5, 12, -3, 0, -8, 7]
    print("\nArray with negative numbers:", arr7)
    print("Sorted array:", merge_sort(arr7))


# Run the tests
test_merge_sort()
