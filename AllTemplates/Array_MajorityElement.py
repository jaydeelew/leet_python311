# Given an array nums of size n, return the majority element.
# The majority element is the element that appears more than n/2 times.
# You may assume that the majority element always exists in the array.
from collections import Counter


def majorityElement(nums: list[int]) -> int:
    candidate = nums[0]
    count = 0

    for n in nums:
        if count == 0:
            candidate = n
        count += 1 if candidate == n else -1

    return candidate

    # Time Complexity: O(n), where n is the length of the input array nums.
    # This is because we iterate through the array once, performing constant time operations at each step.
    #
    # Space Complexity: O(1), as we only use a constant amount of extra space to store the candidate and count variables.


def majorityElement2(nums):
    counts = Counter(nums)
    return max(counts.keys(), key=lambda x: counts[x])

    # Time Complexity: O(n), where n is the length of the input array nums.
    # This is because we iterate through the array once to create the Counter object,
    # and then find the maximum value in the Counter, which takes O(n) time in the worst case.
    #
    # Space Complexity: O(n), as we create a Counter object (counts) to store the count of each unique element in the array.
    # In the worst case, if all elements in the array are unique,
    # the size of the Counter object will be equal to the size of the input array.


nums = [2, 2, 1, 1, 1, 2, 2]
# Output: 2

print(majorityElement(nums))
print(majorityElement2(nums))
