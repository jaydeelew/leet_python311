# def fn(arr):
#     tab = [0] * len(arr)
#     tab[BASE_CASE] = VALUE

#     for i in arr:
#         tab[i] = RECURRENCE_RELATION

#     return tab[i]

# Given an integer array nums, return the length of the longest strictly increasing subsequence.
# The term strictly means that there are not any duplicates in the subsequence.
# Solve using a bottom-Up/iterative tabulation method.


# as we iterate through the array, we keep track of the longest strictly increasing subsequence
# at each index, and at the end, we return the longest (max) strictly increasing subsequence
def len_of_LSIS_iterative(nums: list[int]) -> int:
    # this is where we store the longest strictly increasing subsequence ending at each index
    tab = [1] * len(nums)
    # we start the range with 1 since tab[0] = 1 wll remain unchanged
    for i in range(1, len(nums)):
        for j in range(i):
            if nums[j] < nums[i]:
                # the plus one in tab[j] + 1 represents the current index i.
                # tab[i] may be assigned various increasing values, hence the need to take the max
                tab[i] = max(tab[i], tab[j] + 1)

    return max(tab)


# nums = [10, 9, 2, 5, 3, 7, 101, 18]
# Output: 4

nums = [0, 1, 0, 3, 2, 3]
# Output: 4

# nums = [7, 8, 1, 2, 3]
# Output: 3

# nums = [7, 7, 7, 7, 7, 7, 7]
# Output: 1

print(len_of_LSIS_iterative(nums))
