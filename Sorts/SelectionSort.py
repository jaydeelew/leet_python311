def selection_sort(arr):
    arr = arr.copy()  # Make a copy to not modify the original array
    n = len(arr)
    for i in range(n):
        # Assume the current i is the index of the minimum
        min_index = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_index]:
                min_index = j
        # Swap the found minimum element with the first element
        arr[i], arr[min_index] = arr[min_index], arr[i]
    return arr


def test_selection_sort():
    # Test case 1: Normal array
    arr1 = [64, 34, 25, 12, 22, 11, 90]
    print("Original array:", arr1)
    print("Sorted array:", selection_sort(arr1))

    # Test case 2: Array with duplicates
    arr2 = [5, 2, 8, 5, 1, 9, 2, 8]
    print("\nArray with duplicates:", arr2)
    print("Sorted array:", selection_sort(arr2))

    # Test case 3: Empty array
    arr3 = []
    print("\nEmpty array:", arr3)
    print("Sorted array:", selection_sort(arr3))

    # Test case 4: Single element array
    arr4 = [42]
    print("\nSingle element array:", arr4)
    print("Sorted array:", selection_sort(arr4))

    # Test case 5: Already sorted array
    arr5 = [1, 2, 3, 4, 5]
    print("\nAlready sorted array:", arr5)
    print("Sorted array:", selection_sort(arr5))

    # Test case 6: Reverse sorted array
    arr6 = [5, 4, 3, 2, 1]
    print("\nReverse sorted array:", arr6)
    print("Sorted array:", selection_sort(arr6))

    # Test case 7: Array with negative numbers
    arr7 = [-5, 12, -3, 0, -8, 7]
    print("\nArray with negative numbers:", arr7)
    print("Sorted array:", selection_sort(arr7))


if __name__ == "__main__":
    test_selection_sort()
