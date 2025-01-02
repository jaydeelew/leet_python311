# 367. Valid Perfect Square
# Given a positive integer num, return true if num is a perfect square or false otherwise.
# A perfect square is an integer that is the square of an integer.
# In other words, it is the product of some integer with itself.
# You must not use any built-in library function, such as sqrt.


def isPerfectSquare(num):
    if num < 2:
        return True  # Directly return True for 0 and 1

    left = 2
    right = num // 2

    # we also need left equal to right since the left and right will merge on the square root
    while left <= right:
        mid = (left + right) // 2
        mid_squared = mid**2
        if mid_squared == num:
            return True
        if mid_squared > num:
            right = mid - 1
        else:
            left = mid + 1

    return False


print(isPerfectSquare(7))
print(isPerfectSquare(16))
print(isPerfectSquare(0))
print(isPerfectSquare(1))
