# This function uses a binary search approach to find the maximum element in the array that satisfies the condition.
# It assumes the array is sorted.
# the maximum indicates that all values after it would not meet the condition,
# and all values before it, including the maximum, would meet the condition
def find_maximum_with_condition(arr, condition):
    left = 0
    right = len(arr) - 1

    while left < right:
        # the plus one is to avoid infinite loop by right biasing mid
        mid = (left + right + 1) // 2
        if condition(arr[mid]):
            # if the condition is met, we know that all values to the left of arr[mid] will also be met.
            # therefore, the maximum value is either arr[mid] or to the right of arr[mid]
            left = mid
        else:
            # if the condition is not met, the maximum value is in the left half and excludes arr[mid]
            right = mid - 1

    return arr[right]


arr = [1, 3, 5, 7, 9, 11]
condition = lambda x: x < 10  # noqa: E731
result = find_maximum_with_condition(arr, condition)
print("The maximum value satisfying the condition is:", result)
