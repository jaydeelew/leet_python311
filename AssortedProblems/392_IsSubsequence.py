# Given two strings s and t, return true if s is a subsequence of t, or false otherwise.
# A subsequence of a string is a new string that is formed from the original string by
# deleting some (can be none) of the characters without disturbing the relative positions
# of the remaining characters. (i.e., "ace" is a subsequence of "abcde" while "aec" is not).


def isSubsequence(s, t):
    # Early return if s is an empty set which is always a subset
    if len(s) == 0:
        return True

    # Early return if t is shorter than s
    if len(t) < len(s):
        return False

    i = 0
    for char in t:
        if char == s[i]:
            i += 1
            if i == len(s):
                return True

    return False


# s = "abc"
# t = "ahbgdc"
# Output: True

# s = "axc"
# t = "ahbgdc"
# Output: False

s = ""
t = "gfegee"

print(isSubsequence(s, t))
