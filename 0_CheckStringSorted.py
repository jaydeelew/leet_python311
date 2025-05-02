# 0. Check String Sorted
# Given a string of alphabet characters, check if string is in strictly ascending sorted order.
# Return True or False.


def checkStringSorted(s: str) -> bool:
    if len(s) <= 1:
        return True

    for i in range(1, len(s)):
        if s[i] <= s[i - 1]:
            return False

    return True


str = "acdgpyz"
# Output: True

print(checkStringSorted(str))

# Test cases
test_cases = [
    ("acdgpyz", True),  # Original test case - strictly ascending
    ("a", True),  # Single character
    ("", True),  # Empty string
    ("abc", True),  # Simple ascending
    ("aaa", False),  # All same characters
    ("cba", False),  # Descending order
    ("abca", False),  # Not strictly ascending
    ("abcdefgh", True),  # Long ascending sequence
    ("aBcD", False),  # Mixed case (assuming case matters)
]

# Run tests
for test_str, expected in test_cases:
    result = checkStringSorted(test_str)
    print(f"Test case: '{test_str}'")
    print(f"Expected: {expected}, Got: {result}")
    print(f"Test {'passed' if result == expected else 'failed'}")
    print()
