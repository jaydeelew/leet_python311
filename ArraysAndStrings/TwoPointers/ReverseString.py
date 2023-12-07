# Write a function that reverses a string. The input string is given as an array of characters s.
# You must do this by modifying the input array in-place with O(1) extra memory.


def reverseString(s):
    left = 0
    right = len(s) - 1
    while left < right:
        s[left], s[right] = s[right], s[left]
        left += 1
        right -= 1


s = ["h", "e", "l", "l", "o"]
# Output: ['o', 'l', 'l', 'e', 'h']

reverseString(s)
print(s)
