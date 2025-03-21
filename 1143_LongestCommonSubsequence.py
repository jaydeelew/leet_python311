# 1143. Longest Common Subsequence
# Given two strings text1 and text2, return the length of their longest common subsequence.
# If there is no common subsequence, return 0.
# A subsequence of a string is a new string generated from the original string with some
# characters (can be none) deleted without changing the relative order of the remaining characters.
# For example, "ace" is a subsequence of "abcde".
# A common subsequence of two strings is a subsequence that is common to both strings.


# Bottom Up (iterative)
def longest_common_subsequence(text1, text2):
    rows = len(text1)
    cols = len(text2)

    # Create a matrix with an extra row and column for the base case.
    # The base case is when one of the strings is empty, the longest common subsequence is 0.
    dp = [[0] * (cols + 1) for _ in range(rows + 1)]

    # Fill the dp matrix
    for i in range(rows):
        for j in range(cols):
            if text1[i] == text2[j]:
                # If characters match, add 1 to the previous diagonal value.
                dp[i + 1][j + 1] = dp[i][j] + 1
            else:
                # If they don't match, take the maximum of the cell above or to the left.
                dp[i + 1][j + 1] = max(dp[i + 1][j], dp[i][j + 1])

    return dp[rows][cols]


# Recursive
def longest_common_subsequence_2(text1, text2):
    m = len(text1)
    n = len(text2)

    def lcs(m, n):
        if m == 0 or n == 0:
            result = 0
        elif text1[m - 1] == text2[n - 1]:
            result = 1 + lcs(m - 1, n - 1)
        elif text1[m - 1] != text2[n - 1]:
            temp1 = lcs(m - 1, n)
            temp2 = lcs(m, n - 1)
            result = max(temp1, temp2)

        return result

    return lcs(m, n)


# Top Down (recursive with memoization)
def longest_common_subsequence_3(text1, text2):
    memo = {}

    def lcs(m, n):
        if (m, n) in memo:
            return memo[(m, n)]

        if m == 0 or n == 0:
            result = 0
        elif text1[m - 1] == text2[n - 1]:
            result = 1 + lcs(m - 1, n - 1)
        else:
            result = max(lcs(m - 1, n), lcs(m, n - 1))

        memo[(m, n)] = result
        return result

    return lcs(len(text1), len(text2))


s1 = "abc"
s2 = "ac"
# Output: 2

# s1 = "ABCBDAB"
# s2 = "BDCABC"
# Output: 4

print(longest_common_subsequence(s1, s2))
print(longest_common_subsequence_2(s1, s2))
print(longest_common_subsequence_3(s1, s2))
