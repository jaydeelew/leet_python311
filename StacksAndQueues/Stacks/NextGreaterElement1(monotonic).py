# The next greater element of some element x in an array is the first greater element that is to the right of x in the same array.

# You are given two distinct 0-indexed integer arrays nums1 and nums2, where nums1 is a subset of nums2.

# For each 0 <= i < nums1.length, find the index j such that nums1[i] == nums2[j]
# and determine the next greater element of nums2[j] in nums2.
# If there is no next greater element, then the answer for this query is -1.


class Solution:
    def nextGreaterElement(self, nums1: list[int], nums2: list[int]) -> list[int]:
        stack = []
        dic = {}
        ans = []

        if len(nums2) == 1:
            ans.append(-1)
            return ans

        stack.append(0)  # push zero onto stack
        for i in range(len(nums2) - 1, -1, -1):  # range(start, stop, step) - going backward through array
            # monotonic decreasing stack
            while stack and nums2[i] > stack[-1]:  # keep popping stack while arr element is > than top of stack
                stack.pop()
            if stack:  # if stack not empty, current arr element is less than top of stack indicating that the top of stack
                # is the next greater element for the current arr element
                dic[nums2[i]] = stack[-1]  # for the current arr, assign its next-greater-element (top of stack)
            else:
                dic[nums2[i]] = -1  # since stack empty, current arr element does not have a next-greater-element
            stack.append(nums2[i])  # push current arr element onto stack

        # go through subset array, nums1, and build answer array by appending each values next-greater-element
        for num in nums1:
            ans.append(dic.get(num))

        return ans


# nums1 = [4, 1, 2]
# nums2 = [1, 3, 4, 2]
# Output: [-1,3,-1]

# nums1 = [2, 4]
# nums2 = [1, 2, 3, 4]
# Output: [3,-1]

nums1 = [0]
nums2 = [0]
# Output: [-1]

sol = Solution()
print(sol.nextGreaterElement(nums1, nums2))
