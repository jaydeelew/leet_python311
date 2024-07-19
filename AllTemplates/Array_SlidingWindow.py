# def fn(arr):
#     left = ans = curr = 0

#     for right in range(len(arr)):
#         # do logic here to add arr[right] to curr

#         while WINDOW_CONDITION_BROKEN:
#             # remove arr[left] from curr
#             left += 1

#         # update ans

#     return ans


# Given an array of positive integers nums and an integer k
# find the length of the longest subarray whose sum is less than or equal to k.
def find_longest_subarray(nums, k):
    longest = curr_sum = left = 0

    for right in range(len(nums)):
        curr_sum += nums[right]

        while curr_sum > k:
            curr_sum -= nums[left]
            left += 1

        longest = max(longest, right - left + 1)

    return longest


nums = [3, 1, 2, 7, 4, 2, 1, 1, 5]
k = 8
# Output: 4

print(find_longest_subarray(nums, k))
