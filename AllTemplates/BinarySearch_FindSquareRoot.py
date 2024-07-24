# Find the square root of a number using binary search
# If the number is not a perfect square, return the floor of the square root


def findSqrt(num):
    if num < 2:
        return num  # Directly return the number if it's 0 or 1

    left, right = 1, num // 2  # No need to check beyond num // 2 for num > 1

    while left <= right:
        mid = (left + right) // 2
        mid_squared = mid * mid

        if mid_squared == num:
            return mid
        elif mid_squared < num:
            left = mid + 1
        else:
            right = mid - 1

    return right


print(findSqrt(16))
print(findSqrt(17))
print(findSqrt(1))
print(findSqrt(0))
