# Given a string, reverse the string and return the reversed string.


# Method 1: Using slicing
def reverseString(str):
    reversed_string = my_string[::-1]
    return reversed_string

    # Time Complexity: O(n), where n is the length of the string.
    # Space Complexity: O(n), as a new string is created to store the reversed string.


# Method 2: Using two pointers
def reverseString2(str):
    list_of_chars = list(str)  # Convert string to list of characters
    left = 0
    right = len(str) - 1

    while left < right:
        list_of_chars[left], list_of_chars[right] = list_of_chars[right], list_of_chars[left]
        left += 1
        right -= 1

    return "".join(list_of_chars)  # Convert list of characters back to string

    # Time Complexity: O(n), where n is the length of the string.
    # Space Complexity: O(1), since we reverse the string in place.


my_string = "Hello, World!"
print(reverseString(my_string))
print(reverseString2(my_string))
