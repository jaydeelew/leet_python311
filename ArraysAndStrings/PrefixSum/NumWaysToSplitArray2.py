# We can improve to O(1) space while still leveraging the idea of a prefix sum by simply calculating leftSection on the fly.
# The right section's sum must be the total sum minus the left section.


def waysToSplitArray2(nums):
    ans = left_section = 0
    total = sum(nums)  # sum of all element in nums[]

    for i in range(len(nums) - 1):  # from nums[0] to second to last element in nums (need to keep last element for right section)
        left_section += nums[i]  # maintain running sum of left section
        right_section = total - left_section  # total sum of nums[] minus current running sum of left section
        if left_section >= right_section:
            ans += 1

    return ans


nums = [10, 4, -8, 7]
print(waysToSplitArray2(nums))
