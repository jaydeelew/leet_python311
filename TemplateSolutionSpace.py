def find_min_value_that_satisfies_condition(array: list) -> int:
    def condition(value: int) -> bool:
        # when looking for minimum, all values >= min value will be True
        # all values less than min value will be False
        return True if value >= 5 else False

    left = min(array)
    right = max(array)
    while left <= right:
        mid = left + (right - left) // 2
        if condition(mid):
            right = mid - 1
        else:
            left = mid + 1
    return left


def find_max_value_that_satisfies_condition(array: list) -> int:
    def condition(value: int) -> bool:
        # when looking for maximum, all values <= max value will be True
        # all values greater than max value will be False
        return True if value <= 5 else False

    left = min(array)
    right = max(array)
    while left <= right:
        mid = left + (right - left) // 2
        if condition(mid):
            left = mid + 1
        else:
            right = mid - 1
    return right


array = [8, 3, 7, 2, 1, 0, 6, 9, 4]

print(find_min_value_that_satisfies_condition(array))  # returns 5
print(find_max_value_that_satisfies_condition(array))  # returns 5
