# Example 1: Return true if a given string is a palindrome, false otherwise.
# A string is a palindrome if it reads the same forwards as backwards.
# That means, after reversing it, it is still the same string. For example: "abcdcba", or "racecar".


def check_if_palindrome(s):
    left = 0  # left boundary pointer
    right = len(s) - 1  # right boundary pointer

    while left < right:
        if s[left] != s[right]:  # if left and right pointers are not equal
            return False  # not a palindrome
        left += 1  # move left boundary pointer toward the center once
        right -= 1  # move right boundary pointer toward the center once

    return True


s = "racecar"
print(check_if_palindrome(s))
