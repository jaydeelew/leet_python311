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


def test_insertion_sort():
    # Test case 1: Normal array
    arr1 = [64, 34, 25, 12, 22, 11, 90]
    print("Original array:", arr1)
    print("Sorted array:", insertion_sort(arr1))

    # Test case 2: Array with duplicates
    arr2 = [5, 2, 8, 5, 1, 9, 2, 8]
    print("\nArray with duplicates:", arr2)
    print("Sorted array:", insertion_sort(arr2))

    # Test case 3: Empty array
    arr3 = []
    print("\nEmpty array:", arr3)
    print("Sorted array:", insertion_sort(arr3))

    # Test case 4: Single element array
    arr4 = [42]
    print("\nSingle element array:", arr4)
    print("Sorted array:", insertion_sort(arr4))

    # Test case 5: Already sorted array
    arr5 = [1, 2, 3, 4, 5]
    print("\nAlready sorted array:", arr5)
    print("Sorted array:", insertion_sort(arr5))

    # Test case 6: Reverse sorted array
    arr6 = [5, 4, 3, 2, 1]
    print("\nReverse sorted array:", arr6)
    print("Sorted array:", insertion_sort(arr6))

    # Test case 7: Array with negative numbers
    arr7 = [-5, 12, -3, 0, -8, 7]
    print("\nArray with negative numbers:", arr7)
    print("Sorted array:", insertion_sort(arr7))


# Run the tests
if __name__ == "__main__":
    test_insertion_sort()
