# 496. Given an array, find the Next Greater Element for every element.
# The Next Greater Element for an element is the first greater element on the right side of the array.
# Elements for which no greater element exist, consider the next greater element as -1.


class NextGreater:
    def next_greater_elements(self, arr):
        stack = []
        # create array of zeroes to index into later
        output = [0] * len(arr)
        # push a zero onto stack
        stack.append(0)
        # range(start, stop, step): start at last index, stop at zero index, step back one index at a time
        for i in range(len(arr) - 1, -1, -1):
            # pop stack if arr element is >= to top of stack
            while stack and arr[i] >= stack[-1]:
                stack.pop()
            # if stack not empty, current arr element is less than top of stack indicating that the top of stack
            # is the next greater element for the current arr element
            if stack:
                # for the current arr element postion, assign its next-greater-element (top of stack)
                output[i] = stack[-1]
            else:
                # since stack empty, current arr element does not have a next-greater-element
                output[i] = -1
            # push current arr element onto stack
            stack.append(arr[i])
        return output


arr = [3, 2, 8, 7, 9, 17, 12]  # Output: [8, 8, 9, 9, 17, -1, -1]
# arr = [4, 5, 2, 25]  # Output: [5,25,25,-1]
# arr = [13, 7, 6, 12]  # Output: [-1,12,12,-1]
# arr = [1, 2, 3]  # Output: [2,3,-1]
# arr = [3, 2, 1]  # Output: [-1,-1,-1]

size = len(arr)
ng = NextGreater()
print(ng.next_greater_elements(arr))
