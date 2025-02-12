# 0. Monotonically Increasing Stack


class IncreasingStack:
    def build_stack(self, arr):
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
arr_sz = len(arr)
# Output: [1, 3, 10]

inc_stack = IncreasingStack()
print(inc_stack.build_stack(arr))
