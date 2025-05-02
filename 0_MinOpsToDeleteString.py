# 0. Minimum Operations to Delete String
# Given a string, str, you are allowed to delete contiguous characters
# if all the characters are the same in a single operation.
# For characters that are not adjacent to the same character, these can only be removed one at a time.
# The task is to find the minimum number of operations required to completely delete the string.


def min_operations_to_delete(s: str) -> int:
    if not s:
        return 0

    operations = 0

    # Keep processing until string is empty
    while s:
        # Find the longest continuous same character sequence
        max_len = 1
        curr_len = 1
        for i in range(1, len(s)):
            if s[i] == s[i - 1]:
                curr_len += 1
                max_len = max(max_len, curr_len)
            else:
                curr_len = 1

        # If no groups found (max_len = 1), remove one character
        if max_len == 1:
            operations += 1
            s = s[1:]
        else:
            # Find and remove the first longest group
            curr_len = 1
            for i in range(1, len(s)):
                if s[i] == s[i - 1]:
                    curr_len += 1
                    if curr_len == max_len:
                        # Remove this group
                        s = s[: i - max_len + 1] + s[i + 1 :]  # noqa
                        operations += 1
                        break
                else:
                    curr_len = 1

    return operations


str = "abcddcba"
# Output: 4

# str = "abc"
# Output: 3

print(min_operations_to_delete(str))

# Test cases
test_cases = [
    ("abcddcba", 4),  # Original test case
    ("abc", 3),  # No groups, all single deletions
    ("aabbcc", 3),  # Three groups of two
    ("aaabbb", 2),  # Two groups of three
    ("aaaa", 1),  # Single group of four
    ("", 0),  # Empty string
    ("a", 1),  # Single character
    ("ababab", 6),  # No groups, all single deletions
    ("aabbaa", 3),  # Groups form after deletions
    ("aabbaacc", 4),  # Multiple groups
]

# Run tests
for test_str, expected in test_cases:
    result = min_operations_to_delete(test_str)
    print(f"Test case: '{test_str}'")
    print(f"Expected: {expected}, Got: {result}")
    print(f"Test {'passed' if result == expected else 'failed'}")
    print()
