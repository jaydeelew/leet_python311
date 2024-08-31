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

    # Time Complexity: O(n), where n is the length of the input array nums.
    # This is because we iterate through the array once using the right pointer,
    # and the left pointer moves at most n steps in total. Therefore, O(2n) is O(n).
    #
    # Space Complexity: O(1), as we only use a constant amount of extra space
    # to store the variables longest, curr_sum, left, and right.


nums = [3, 1, 2, 7, 4, 2, 1, 1, 5]
k = 8
# Output: 4

print(find_longest_subarray(nums, k))


# Given an array of integers and an integer k, return the number of subarrays
# where the sum of the elements in the subarray equals k.
def count_subarrays_with_sum_k(nums, k):
    count = curr_sum = left = 0

    for right in range(len(nums)):
        curr_sum += nums[right]

        while curr_sum > k:
            curr_sum -= nums[left]
            left += 1

        if curr_sum == k:
            count += 1
            # we need to remove the left element from the sum
            # because when the right pointer moves and the next element is added
            # the sum will be greater than k
            curr_sum -= nums[left]
            left += 1

    return count

    # Time Complexity: O(n), where n is the length of the input array nums.
    # This is because we iterate through the array once using the right pointer,
    # and the left pointer moves at most n steps in total Therefore, O(2n) is O(n).
    #
    # Space Complexity: O(1), as we only use a constant amount of extra space
    # to store the variables count, curr_sum, left, and right.


nums = [1, 2, 3, 4, 5]
k = 3
# Output: 2

print(count_subarrays_with_sum_k(nums, k))
