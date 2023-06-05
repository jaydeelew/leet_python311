# Example 4: Is Subsequence.
# Given two strings s and t, return true if s is a subsequence of t, or false otherwise.

# A subsequence of a string is a new string that is formed from the original string
# by deleting some (can be none) of the characters without disturbing the relative positions
# of the remaining characters. (i.e., "ace" is a subsequence of "abcde" while "aec" is not).


def isSubsequence(s, t):
    i = j = 0  # the initial indexes of strings s & t
    while i < len(s) and j < len(t):  # while the indexes do not exceed the lengths of s & t
        # if currently pointed to elements of s & t match, increment i
        if s[i] == t[j]:
            i += 1
        j += 1  # increment j

    return i == len(s)  # if i equals length of s, all of s was traversed and therefore a subset of t


s = "ace"
t = "abcde"
print(isSubsequence(s, t))
