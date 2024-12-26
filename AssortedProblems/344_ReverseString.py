# 344. Reverse String
# Write a function that reverses an array. The input is given as an array of characters s.
# You must do this by modifying the input array in-place with O(1) extra memory.


def reverseString(arr):
    left = 0
    right = len(arr) - 1
    while left < right:
        arr[left], arr[right] = arr[right], arr[left]
        left += 1
        right -= 1
    return arr

    # Time Complexity: O(n), where n is the length of the input array arr.
    # This is because we iterate through half of the array, performing constant time operations at each step.

    # Space Complexity: O(1), as we modify the input array in-place without using any additional space.


chars = ["h", "e", "l", "l", "o"]
# Output: ['o', 'l', 'l', 'e', 'h']

nums = [1, 2, 3, 4, 5]
# Output: [5, 4, 3, 2, 1]

print(reverseString(chars))
print(reverseString(nums))
