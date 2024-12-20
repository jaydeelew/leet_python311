# Given a sorted array and a condition, find the minimum value in the array that satisfies the condition
# When finding the minimum, all values after it, including the minimum, would meet the condition,
# and all values before it would not meet the condition.
# This assumes the array is sorted.


def find_min(arr, condition):
    if not arr:
        return None

    left = 0
    right = len(arr) - 1

    # Check if any element satisfies the condition
    if not condition(arr[right]):
        return None

    # Check if all elements satisfy the condition
    if condition(arr[left]):
        return arr[left]

    while left < right:
        mid = (left + right) // 2
        if condition(arr[mid]):
            right = mid
        else:
            left = mid + 1

    return arr[left]


test_cases = [
    ([1, 3, 5, 7, 9], lambda x: x > 6, "x > 6"),  # Normal case
    ([1, 2, 3], lambda x: x > 10, "x > 10"),  # No element satisfies
    ([5, 6, 7], lambda x: x > 0, "x > 0"),  # All elements satisfy
    ([1], lambda x: x > 0, "x > 0"),  # One element that satisfies
    ([1], lambda x: x > 1, "x > 1"),  # ONe element that does not satify
]

for arr, condition, condition_str in test_cases:
    print(f"Array: {arr}, Condition: {condition_str}, Result: {find_min(arr, condition)}")
