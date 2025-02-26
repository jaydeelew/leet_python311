# 392. Is Subsequence
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


def isSubsequence_2(s, t):
    # Early return if s is an empty set which is always a subset.
    if len(s) == 0:
        return True

    # Early return if t is shorter than s.
    if len(t) < len(s):
        return False

    i = j = 0
    while i < len(s) and j < len(t):
        if s[i] == t[j]:
            i += 1
        j += 1
    return i == len(s)


def isSubsequence_3(s, t):
    iter_t = iter(t)
    # For each char in s, next(iter_t) is called until there is either a match
    # with char in iter_t, which will pause iteration and continue to the next char in s, or until iter_t
    # raises a StopIteration exception when it reaches the end of iter_t.
    # If all chars from s are found in iter_t, True is returned, otherwise False.
    return all(char in iter_t for char in s)


s = "abc"
t = "ahbgdc"
Output: True

# s = "axc"
# t = "ahbgdc"
# Output: False

# s = ""
# t = "gfegee"

print(isSubsequence(s, t))
print(isSubsequence_2(s, t))
print(isSubsequence_3(s, t))
