# 0. Find Minimum Value That Satisfies a Condition
# Given a sorted array and a condition, find the minimum value in the array that satisfies the condition
# When finding the minimum, all values after it, including the minimum, would meet the condition,
# and all values before it would not meet the condition.
# This assumes the array is sorted.


def find_min(arr, condition):
    if not arr:
        return None

    # If the last element does not meet the condition,
    # all other items to the left will not meet the condition.
    if not condition(arr[-1]):
        return None

    # If the first element meets the condition,
    # all other elements meet the condition and therefore the first element is the max.
    if condition(arr[0]):
        return arr[0]

    left = 0
    right = len(arr) - 1

    while left < right:
        mid = (left + right) // 2
        if condition(arr[mid]):
            # Bring right to mid and not mid - 1 since mid may be the mininum
            right = mid
        else:
            # Condition failed, so mid is not the mininum
            left = mid + 1

    return arr[left]


tests = [
    ([1, 3, 5, 7, 9], lambda x: x > 6, "x > 6: Normal case", 7),
    ([1, 2, 3], lambda x: x > 10, "x > 10: No element satisfies", None),
    ([5, 6, 7], lambda x: x > 0, "x > 0: All elements satisfy", 5),
    ([1], lambda x: x > 0, "x > 0: One element satisfies", 1),
    ([1], lambda x: x > 1, "x > 1: One element does not satisfy", None),
    ([], lambda x: x > 1, "x > 1: No elements in array", None),
]

for arr, cond, desc, excepted in tests:
    print(f"{arr}, {desc}, Expect: {excepted}, {find_min(arr, cond) == excepted}")
