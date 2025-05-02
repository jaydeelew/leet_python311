# 0. Find All Palindromes
# Given a string s, find all palindromes in the string with a length of 3 or greater.


def find_all_palindromes(s):
    if not s:
        return []

    palindromes = set()  # Using set to avoid duplicates

    def expand_around_center(left, right):
        # Expand while we're within bounds and characters match
        while left >= 0 and right < len(s) and s[left] == s[right]:
            # Only add palindromes of length 3 or more
            if right - left + 1 >= 3:
                palindromes.add(s[left : right + 1])  # noqa
            left -= 1
            right += 1

    # Check all possible centers
    for i in range(len(s)):
        # Odd length palindromes
        expand_around_center(i, i)
        # Even length palindromes
        expand_around_center(i, i + 1)

    return list(palindromes)


# Test cases with their expected results
test_cases = {
    "racecar": {"racecar", "aceca", "cec"},  # Multiple palindromes of different lengths
    "babad": {"bab", "aba"},  # Two overlapping palindromes
    "aaa": {"aaa"},  # Single palindrome
    "abba": {"abba"},  # Even length palindrome
    "hello": set(),  # No palindromes
    "aaaaa": {"aaaaa", "aaaa", "aaa"},  # Nested palindromes
    "dabacfqadd": {"aba"},  # Single palindrome within string
}

for test_str, expected in test_cases.items():
    result = set(find_all_palindromes(test_str))
    assert result == expected, f"\nString: {test_str}\nExpected: {expected}\nGot: {result}"
print("All test cases passed!")
