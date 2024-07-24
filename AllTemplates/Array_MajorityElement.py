# Given an array nums of size n, return the majority element.
# The majority element is the element that appears more than n / 2 times.
# You may assume that the majority element always exists in the array.
from collections import Counter


# The majorityElement function uses the Boyer-Moore Voting Algorithm.
# Time Complexity: O(n), where n is the number of elements in the array.
# Space Complexity: O(1), as it uses only a few extra variables.
def majorityElement(nums: list[int]) -> int:
    candidate = nums[0]
    count = 0

    for n in nums:
        if count == 0:
            candidate = n
        count += 1 if candidate == n else -1

    return candidate


# The majorityElement2 function uses a Counter to count the occurrences of each element.
# Time Complexity: O(n), where n is the number of elements in the array.
# Space Complexity: O(n), as it uses a dictionary to store the counts of each element.
def majorityElement2(nums):
    counts = Counter(nums)
    # counts.get sets the key to compare to the values of counts instead of the default of key for a dictionary
    return max(counts, key=counts.get)


nums = [2, 2, 1, 1, 1, 2, 2]
# Output: 2

print(majorityElement(nums))
print(majorityElement2(nums))
