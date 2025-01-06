# 2270. We can improve to O(1) space while still leveraging the idea of a prefix sum by simply calculating leftSection on the fly.
# The right section's sum must be the total sum minus the left section.


def waysToSplitArray2(nums):
    ans = left_section = 0
    total = sum(nums)

    # from nums[0] to second to last element in nums (need to keep last element for right section)
    for i in range(len(nums) - 1):
        # maintain running sum of left section
        left_section += nums[i]
        # total sum of nums[] minus current running sum of left section
        right_section = total - left_section
        if left_section >= right_section:
            ans += 1

    return ans


nums = [10, 4, -8, 7]
# Output: 2

print(waysToSplitArray2(nums))
