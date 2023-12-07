# Return true if a given string is a palindrome, false otherwise.
# A string is a palindrome if it reads the same forwards as backwards.
# That means, after reversing it, it is still the same string. For example: "abcdcba", or "racecar".


def check_if_palindrome(s):
    left = 0
    right = len(s) - 1

    while left < right:
        # if left and right pointers are not equal
        if s[left] != s[right]:
            # not a palindrome
            return False
        left += 1
        right -= 1

    return True


s = "racecar"
# Output: True

print(check_if_palindrome(s))
