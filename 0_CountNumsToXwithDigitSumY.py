# 0. Count Numbers to x with Digit Sum y
# Given two numbers x and y, count how many numbers from 1 to x (inclusive) have digits that sum to y
# For example, if x = 25 and y = 5:
# - 5 (sum of digits = 5)
# - 14 (sum of digits = 1 + 4 = 5)
# - 23 (sum of digits = 2 + 3 = 5)
# Output: 3
from functools import cache


# Brute Force
def countNumbers_1(x, y):
    def digit_sum(n):
        return sum(int(digit) for digit in str(n))

    count = 0
    for i in range(1, x + 1):
        if digit_sum(i) == y:
            count += 1

    return count


# Dynamic Programming
def countNumbers_2(num, target):
    # Convert input number to list of digits for processing
    digits = list(map(int, str(num)))
    num_len = len(digits)

    @cache  # Memoize results to avoid recomputing same subproblems
    def dp(digit_pos, bounded, curr_sum):
        # Base case: if we've processed all digits
        if digit_pos == num_len:
            return 1 if curr_sum == target else 0

        ans = 0
        # If bounded is True, we can only use digits up to digits[digit_pos]
        # If bounded is False, we can use any digit from 0-9
        max_digit = digits[digit_pos] if bounded else 9

        # Try each valid digit at current position
        for d in range(0, max_digit + 1):
            # If adding this digit would exceed target sum, we can break
            # since all subsequent digits will also exceed the target
            if curr_sum + d > target:
                break

            # Recursively count valid numbers:
            # - Move to next position (digit_pos + 1)
            # - Update bounded flag: remains bounded only if we're already bounded AND using max digit
            # - Add current digit to running sum
            new_bounded = bounded and (d == max_digit)
            ans += dp(digit_pos + 1, new_bounded, curr_sum + d)

        return ans

    # Start with position 0, bounded constraint True, and sum 0
    return dp(0, True, 0)


x = 11
y = 2
# Output: 2
print(f"Count of numbers <= {x} with digit sum {y}: {countNumbers_1(x, y)}")
print(f"Count of numbers <= {x} with digit sum {y}: {countNumbers_2(x, y)}")
