class IncreasingStack:
    def build_stack(self, arr):
        stack = []
        for num in arr:
            while stack and num >= stack[-1]:
                stack.pop()
            stack.append(num)
        return stack


arr = [15, 17, 14, 12, 13, 14, 10]
inc_stack = IncreasingStack()
print(inc_stack.build_stack(arr))
