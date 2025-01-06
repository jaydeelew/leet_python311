# A monotonically decreasing stack


class DescreasingStack:
    def build_stack(self, arr, arr_sz):
        stack = []
        for element in arr:
            # keep popping elements from the stack as long as there is a stack
            # and the current element is greater or equal to the element at the top of the stack
            while stack and element >= stack[-1]:
                stack.pop()
            # push the current element onto the stack.
            stack.append(element)
        return stack


arr = [15, 17, 14, 12, 13, 14, 10]
arr_sz = len(arr)
# Output: [17, 14, 10]

dec_stack = DescreasingStack()
print(dec_stack.build_stack(arr, arr_sz))
