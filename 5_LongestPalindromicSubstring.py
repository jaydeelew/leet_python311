# 5. Longest Palindromic Substring
# Given a string s, return the longest palindromic substring in s.


def longestPalindrom(s):
    if not s:
        return ""

    start = 0  # Starting index of the longest palindrome
    max_len = 1  # Length of the longest palindrome

    def expand_around_center(left, right):
        # Expand while we're within bounds and characters match
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
        # Return the length of palindrome found
        return right - left - 1

    # Iterate through each character as a potential center
    for i in range(len(s)):
        # Check odd length palindromes (center is a single character)
        len1 = expand_around_center(i, i)
        # Check even length palindromes (center is between two characters)
        len2 = expand_around_center(i, i + 1)

        # Update if we found a longer palindrome
        curr_max_len = max(len1, len2)
        if curr_max_len > max_len:
            max_len = curr_max_len
            # Calculate the starting point of the palindrome
            # by subtracting half the length of the palindrome from the center, i.
            # The -1 takes into consideration even-lengthed palindromes.
            start = i - (curr_max_len - 1) // 2

    return s[start : start + max_len]  # noqa


s = "dabacfqadd"
# Output: "aba"

# s = "babad"
# Output: "bab", "aba" is also a valid answer.

# s = "cbbd"
# Output: "bb"

print(longestPalindrom(s))
