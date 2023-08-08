class DescreasingStack:
    def build_stack(self, arr, arr_sz):
        stack = []
        for num in arr:
            while stack and num <= stack[-1]:
                stack.pop()
            stack.append(num)
        return stack


arr = [1, 4, 5, 3, 3, 12, 10]
arr_sz = len(arr)
dec_stack = DescreasingStack()
print(dec_stack.build_stack(arr, arr_sz))
