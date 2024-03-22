# def fn(arr):
#     stack = []
#     ans = 0

#     for num in arr:
#         # for monotonic decreasing, just flip the > to <
#         while stack and stack[-1] > num:
#             # do logic
#             stack.pop()
#         stack.append(num)

#     return ans


def build_stack(arr):
    stack = []
    for element in arr:
        # keep popping elements from the stack as long as there is a stack
        # and the current element is less or equal to the element at the top of the stack
        while stack and element <= stack[-1]:
            stack.pop()
        # push the current element onto the stack.
        stack.append(element)
    return stack


arr = [1, 4, 5, 3, 3, 12, 10]
# Output: [1, 3, 10]

print(build_stack(arr))
