# 69. Sqrt(x)
# Given a non-negative integer x, return the square root of x rounded down to the nearest integer.
# The returned integer should be non-negative as well.
# You must not use any built-in exponent function or operator.


def mySqrt(num):
    if num < 2:
        # directly return the number if it's 0 or 1
        return num

    # No need to check beyond num // 2 for num > 1
    left, right = 2, num // 2

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


print(mySqrt(16))
print(mySqrt(17))
print(mySqrt(1))
print(mySqrt(0))
