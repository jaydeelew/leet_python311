# 88. Merge Sorted Array
# You are given two integer arrays nums1 and nums2, sorted in non-decreasing order,
# and two integers m and n, representing the number of elements in nums1 and nums2 respectively.
# Merge nums1 and nums2 into a single array sorted in non-decreasing order.
# The final sorted array should not be returned by the function,
# but instead be stored inside the array nums1. To accommodate this,
# nums1 has a length of m + n, where the first m elements denote the elements that should be merged,
# and the last n elements are set to 0 and should be ignored. nums2 has a length of n.


def merge(nums1, m, nums2, n):
    # Start from the end of nums1
    last = m + n - 1
    # Keep track of the last elements in both arrays
    m = m - 1
    n = n - 1

    # While we still have elements to compare
    while n >= 0:
        if m >= 0 and nums1[m] > nums2[n]:
            nums1[last] = nums1[m]
            m -= 1
        else:
            nums1[last] = nums2[n]
            n -= 1
        last -= 1


nums1 = [1, 2, 3, 0, 0, 0]
m = 3
nums2 = [2, 5, 6]
n = 3
# Output: [1,2,2,3,5,6]
# Explanation: The arrays we are merging are [1,2,3] and [2,5,6].

# nums1 = [1]
# m = 1
# nums2 = []
# n = 0
# Output: [1]
# Explanation: The arrays we are merging are [1] and [].

# nums1 = [0]
# m = 0
# nums2 = [1]
# n = 1
# Output: [1]
# Note that because m = 0, there are no elements in nums1. The 0 is only there to ensure the merge result can fit in nums1.

# nums1 = [2, 0]
# m = 1
# nums2 = [1]
# n = 1
# Output: [1, 2]

# nums1 = [1, 2, 4, 5, 6, 0]
# m = 5
# nums2 = [3]
# n = 1
# Output: [1, 2, 3, 4, 5, 6]

merge(nums1, m, nums2, n)
print(nums1)
