# 0. Find Maximum Value That Satisfies a Condition
# Given a sorted array and a condition, find the maximum value in the array that satisfies the condition.
# A maximum would have all values before it, including the maximum, meet the condition.
# All values after the maximum would not meet the condition.
# This assumes the array is sorted.


def find_max(arr, cond):
    if not arr:
        return None

    # If the first element does not meet the condition,
    # all other items to the right will not meent the condition.
    if not cond(arr[0]):
        return None

    # If the last element meets the condition,
    # all other elements meet the condition and therefore the last is the max element.
    if cond(arr[-1]):
        return arr[-1]

    left = 0
    right = len(arr) - 1

    while left < right:
        # when finding the maximum value that satisfies the condition,
        # we want to be biased toward the right when down to two elements by adding + 1
        # because we're looking for the last true value
        mid = (left + right + 1) // 2

        if cond(arr[mid]):
            left = mid
        else:
            right = mid - 1

    return arr[left]


tests = [
    ([1, 3, 5, 7, 9, 11], lambda x: x < 6, "x < 6: Normal case", 5),
    ([1, 2, 3], lambda x: x > 3, "x > 3: No element satisfies", None),
    ([1, 2, 3], lambda x: x > 0, "x > 0: All elements satisy", 3),
    ([1], lambda x: x < 3, "x < 3: A single element satisfies", 1),
    ([1], lambda x: x > 3, "x > 3: A single element does not satisfy", None),
]

max_len_num = max(len(str(test[0])) for test in tests) + 1
max_len_desc = max(len(str(test[2])) for test in tests) + 1

for input in tests:
    result = find_max(input[0], input[1])
    print(
        f"nums: {str(input[0]):<{max_len_num}}"
        f"Cond: {str(input[2]):<{max_len_desc}}"
        f"Expect: {str(input[3]):<7}"
        f"Result: {result == input[3]}"
    )
