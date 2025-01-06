# 0. Monotonically Increasing Stack
# Given an integer array, return a monotonic increasing stack of the array.


def buildStack(nums):
    stack = []
    for num in nums:
        # keep popping elements from the stack as long as there is a stack
        # and the current element is less or equal to the element at the top of the stack
        while stack and num <= stack[-1]:
            stack.pop()
        # if we were to append num to stack before checking to see if num <= stack[-1],
        # num would always equal the top element of the stack
        stack.append(num)

    return stack


arr = [1, 4, 5, 3, 3, 12, 10]
# Output: [1, 3, 10]

print(buildStack(arr))
