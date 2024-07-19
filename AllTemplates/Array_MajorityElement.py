# Given an array nums of size n, return the majority element.
# The majority element is the element that appears more than n / 2 times.
# You may assume that the majority element always exists in the array.


def majorityElement(nums: list[int]) -> int:
    candidate = nums[0]
    count = 0

    for n in nums:
        if count == 0:
            candidate = n
        count += 1 if candidate == n else -1

    return candidate


nums = [2, 2, 1, 1, 1, 2, 2]
# Output: 2

print(majorityElement(nums))
