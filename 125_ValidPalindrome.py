# 125. Valid Palindrome
# A phrase is a palindrome if, after converting all uppercase letters into lowercase letters
# and removing all non-alphanumeric characters, it reads the same forward and backward.
# Alphanumeric characters include letters and numbers.
# Given a string s, return true if it is a palindrome, or false otherwise.


def isPalindrome(s: str) -> bool:
    # Remove non-alphanumeric characters and convert to lowercase
    cleaned_str = "".join(char.lower() for char in s if char.isalnum())
    # Check if the cleaned string is equal to its reverse
    return cleaned_str == cleaned_str[::-1]


print(isPalindrome("A man, a plan, a canal: Panama"))  # Output: True
print(isPalindrome("race a car"))  # Output: False
print(isPalindrome("racecar"))  # Output: True
