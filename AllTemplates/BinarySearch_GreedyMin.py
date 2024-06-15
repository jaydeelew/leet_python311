# the minimum indicates that all values before it would not meet the condition,
# and all values after it, including the minimum, would meet the condition
def find_minimum_with_condition(arr, condition):
    """
    This function uses a binary search approach to find the minimum element in the array that satisfies the condition.
    It assumes the array is sorted.
    """
    left = 0
    right = len(arr) - 1

    while left < right:
        mid = (left + right) // 2
        if condition(arr[mid]):
            # if the condition is true, the minimum value is in the left half
            # and it might be the mid value
            right = mid
        else:
            # if the condition is false, the minimum value is in the right half
            # and excludes the mid value
            left = mid + 1

    return arr[left]


arr = [1, 3, 5, 7, 9, 11]
condition = lambda x: x > 4  # noqa: E731
result = find_minimum_with_condition(arr, condition)
print("The minimum value satisfying the condition is:", result)
