# Given a string, reverse the string and return the reversed string.


# Method 1: Using slicing
def reverseString(str):
    return str[::-1]
    # Time Complexity: O(n), where n is the length of the string.
    # Space Complexity: O(n), as a new string is created to store the reversed string.


# Method 2: Using reversed()
def reverseString_2(str):
    return "".join(reversed(str))
    # Time Complexity: O(n), where n is the length of the string.
    # Space Complexity: O(n), as a new string is created to store the reversed string.


# Method 3: Using two pointers
def reverseString_3(str):
    list_of_chars = list(str)  # Convert string to list of characters
    left = 0
    right = len(str) - 1

    while left < right:
        list_of_chars[left], list_of_chars[right] = list_of_chars[right], list_of_chars[left]
        left += 1
        right -= 1

    return "".join(list_of_chars)  # Convert list of characters back to string

    # Time Complexity: O(n), where n is the length of the string.
    # Space Complexity: O(n), as a new list of characters is created to store the reversed string.


# Method 4: Using a generator expression
def reverseString_4(str):
    return "".join(str[i] for i in range(len(str) - 1, -1, -1))
    # Time Complexity: O(n), where n is the length of the string.
    # Space Complexity: O(n), as a new string is created to store the reversed string.


my_string = "Hello, World!"

print(reverseString(my_string))
print(reverseString_2(my_string))
print(reverseString_3(my_string))
print(reverseString_4(my_string))
