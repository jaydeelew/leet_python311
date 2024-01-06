# 525. Given a binary array nums, return the maximum length of a contiguous subarray with an equal number of 0 and 1.


class Solution:
    def findMaxLength(self, nums: list[int]) -> int:
        # my_dict = {count: index}
        my_dict = {}
        # count(key), 0, is set to index(value), -1, so that when subtracting -1 from another count of 0 at
        # another index, we will arrive at proper length of the current contiguos subarray w/ equal 0's & 1's.
        my_dict[0] = -1
        count, max_len = 0, 0
        for i in range(len(nums)):
            count += 1 if nums[i] == 1 else -1
            if count in my_dict.keys():
                # if the current count matches an existing count in my_dict,
                # the difference between the current index and the matching-count index
                # is the length of the current subarray with an equal number of 0's and 1's.
                max_len = max(max_len, i - my_dict.get(count))
            else:
                # if this count was never seen before, add the count: index to dictionary
                my_dict[count] = i

        return max_len


# nums = [0, 1]
# # Output: 2

# nums = [0, 1, 0]
# # Output: 2

nums = [1, 1, 1, 1, 0, 1]
# Output: 2

# nums = [1, 1, 1, 0, 0, 0]
# # Output: 6

sol = Solution()
print(sol.findMaxLength(nums))
