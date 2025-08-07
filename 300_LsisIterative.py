# 300. Longest Increasing Subsequence (iterative)
# Given an integer array nums, return the length of the longest strictly increasing subsequence.
# The term strictly means that there are not any duplicates in the subsequence.
# Solve using a bottom-Up/iterative tabulation method.


# As we iterate through the array, we keep track of the longest strictly increasing subsequence
# at each index, and at the end, we return the max lsis from the tabulation array.
def lsisIterative(nums: list[int]) -> int:
    # at each index, we store the longest strictly increasing subsequence.
    tab = [1] * len(nums)
    # we start the range with 1 since tab[0] = 1 wll remain unchanged
    for i in range(1, len(nums)):
        for j in range(i):
            if nums[j] < nums[i]:
                # the "+ 1" in "tab[j] + 1" represents the current index i.
                # tab[i] may be assigned new max values, hence the need to take the max.
                tab[i] = max(tab[i], tab[j] + 1)

    return max(tab)


def lsisOptimal(nums: list[int]) -> int:
    # tails[i] stores the smallest possible tail value for an increasing subsequence of length i+1.
    tails = []

    for num in nums:
        # Binary search for the leftmost position where we can place num.
        left, right = 0, len(tails)
        while left < right:
            mid = (left + right) // 2
            # We are looking for the first element in tails that is greater than or equal to num.
            # The index of this element will be the position where num can replace or extend the subsequence.
            if tails[mid] < num:
                # num is greater than tails[mid], so we move to the right half
                # to find a larger tail value.
                left = mid + 1
            else:
                # num is less than or equal to tails[mid], so we search in the left half
                # and keep mid as a potential position.
                right = mid

        # If left == len(tails), we're extending the longest subsequence
        if left == len(tails):
            tails.append(num)
        else:
            # Replace the element at position 'left' with current num
            tails[left] = num

    return len(tails)


# nums = [10, 9, 2, 5, 3, 7, 101, 18]
# Output: 4

nums = [0, 1, 0, 3, 2, 3]
# Output: 4

# nums = [7, 8, 1, 2, 3]
# Output: 3

# nums = [7, 7, 7, 7, 7, 7, 7]
# Output: 1

print("O(n^2) solution:", lsisIterative(nums))
print("O(n log n) solution:", lsisOptimal(nums))
