# Two pointers: one input, opposite ends

# def fn(arr):
#     left = ans = 0
#     right = len(arr) - 1

#     while left < right:
#         # do some logic here with left and right
#         if CONDITION:
#             left += 1
#         else:
#             right -= 1

#     return ans

# Write a function that reverses a string. The input string is given as an array of characters s.
# You must do this by modifying the input array in-place with O(1) extra memory.


def reverseString(arr):
    left = 0
    right = len(arr) - 1

    while left < right:
        arr[left], arr[right] = arr[right], arr[left]
        left += 1
        right -= 1

    return arr


arr = ["h", "e", "l", "l", "o"]
# Output: ['o', 'l', 'l', 'e', 'h']

print(reverseString(arr))
