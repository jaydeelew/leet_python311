# the maximum indicates that all values after it would not meet the condition,
# and all values before it, including the maximum, would meet the conditi
def find_maximum_with_condition(arr, condition):
    """
    This function uses a binary search approach to find the maximum element in the array that satisfies the condition.
    It assumes the array is sorted.
    """
    left = 0
    right = len(arr) - 1

    while left < right:
        mid = (left + right + 1) // 2
        if condition(arr[mid]):
            # if the condition is true, the maximum value is in the right half
            # and it might be the mid value
            left = mid
        else:
            # if the condition is false, the maximum value is in the left half
            # and excludes the mid value
            right = mid - 1

    return arr[right]


arr = [1, 3, 5, 7, 9, 11]
condition = lambda x: x < 10  # noqa: E731
result = find_maximum_with_condition(arr, condition)
print("The maximum value satisfying the condition is:", result)
