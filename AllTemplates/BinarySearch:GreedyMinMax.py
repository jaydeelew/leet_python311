# If looking for a Minimum:
# def fn(arr):
#     def check(x):
#         # this function is implemented depending on the problem
#         return BOOLEAN
#
#     left = MINIMUM_POSSIBLE_ANSWER
#     right = MAXIMUM_POSSIBLE_ANSWER
#     while left <= right:
#         mid = (left + right) // 2
#         if check(mid):
#             right = mid - 1
#         else:
#             left = mid + 1
#
#     return left


# If looking for a Maximum:
# def fn(arr):
#     def check(x):
#         # this function is implemented depending on the problem
#         return BOOLEAN
#
#     left = MINIMUM_POSSIBLE_ANSWER
#     right = MAXIMUM_POSSIBLE_ANSWER
#     while left <= right:
#         mid = (left + right) // 2
#         if check(mid):
#             left = mid + 1
#         else:
#             right = mid - 1
#
#     return right


# the minimum indicates that all values before it would not meet the condition,
# and all values after it, including the minimum, would meet the condition
def find_minimum_positive(arr):
    """
    This function uses a binary search approach to find the minimum positive number in the array.
    It assumes the array is sorted and contains at least one positive number.
    """

    def condition(value):
        return value >= 0

    left = 0
    right = len(arr) - 1

    # Continue the search until the bounds meet
    while left < right:
        mid = (left + right) // 2
        # Apply the condition to the middle value
        if condition(arr[mid]):
            # If the condition is met, search in the left half
            # we do not want to say right = mid - 1 because arr[mid] may be the minimum value
            right = mid
        else:
            # If the condition is not met, search in the right half
            left = mid + 1

    return arr[left]


# the maximum indicates that all values after it would not meet the condition,
# and all values before it, including the maximum, would meet the condition
def find_maximum_positive(arr):
    """
    This function uses a binary search approach to find the maximum positive number in the array.
    It assumes the array is sorted and contains at least one positive number.
    """

    def condition(value):
        return value >= 0

    left = 0
    right = len(arr) - 1

    # Continue the search until the bounds meet
    while left < right:
        # left + right + 1 to avoid an infinite loop because if condition(arr[mid]) is true
        # and mid equals left, then left is reassigned to mid,
        # causing the loop to repeat without changing the bounds.
        mid = (left + right + 1) // 2
        # Apply the condition to the middle value
        if condition(arr[mid]):
            # If the condition is met, search in the right half
            # we do not want to say left = mid + 1 because arr[mid] may be the maximum value
            left = mid
        else:
            # If the condition is not met, search in the left half
            right = mid - 1

    return arr[right]


arr = [-5, -1, 0, 2, 3, 4, 6]
arr2 = [-10, -5, 5, 10]
arr3 = [-20, -15, -10, -5, 0, 5, 10, 15]

print("Minimum positive value:", find_minimum_positive(arr))
print("Maximum positive value:", find_maximum_positive(arr))

print("Minimum positive value:", find_minimum_positive(arr2))
print("Maximum positive value:", find_maximum_positive(arr2))

print("Minimum positive value:", find_minimum_positive(arr3))
print("Maximum positive value:", find_maximum_positive(arr3))