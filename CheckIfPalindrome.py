# Return true if a given string is a palindrome, false otherwise.
# A string is a palindrome if it reads the same forwards as backwards.
# That means, after reversing it, it is still the same string. For example: "abcdcba", or "racecar".


def check_if_palindrome(arr):
    left = 0
    right = len(arr) - 1

    while left < right:
        # if left and right pointers are not equal
        if arr[left] != arr[right]:
            # not a palindrome
            return False
        left += 1
        right -= 1

    return True


arr = "racecar"
# Output: True

print(check_if_palindrome(arr))
