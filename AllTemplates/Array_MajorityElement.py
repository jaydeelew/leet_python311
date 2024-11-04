# Given an array nums of size n, return the majority element.
# The majority element is the element that appears more than n/2 times.
# You may assume that the majority element always exists in the array.
from collections import Counter, defaultdict


def majorityElement1(nums):
    candidate = None
    count = 0

    for n in nums:
        if count == 0:
            candidate = n
        # the element seen most thus far will always be the candidate
        count += 1 if candidate == n else -1
    # ultimately, the candidate will be the majority element
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


def majorityElement3(nums):
    dict = defaultdict(int)
    for n in nums:
        dict[n] += 1
        if dict[n] > len(nums) / 2:
            return n

    return None

    # Time Complexity: O(n), where n is the length of the input array nums.
    # This is because we iterate through the array once to populate the dictionary,
    # and then potentially iterate through the dictionary to find the majority element,
    # which takes O(n) time in the worst case.
    #
    # Space Complexity: O(n), as we use a dictionary to store the count of each unique element in the array.
    # In the worst case, if all elements in the array are unique,
    # the size of the dictionary will be equal to the size of the input array.


def majorityElement4(nums):
    nums = sorted(nums)
    return nums[len(nums) // 2]

    # Time Complexity: O(n log n), where n is the length of the input array nums.
    # This is because sorting the array takes O(n log n) time.
    #
    # Space Complexity: O(n), as we create a new sorted array, which requires additional space proportional to the size of the input array.


def majorityElement5(nums):
    nums.sort()
    return nums[len(nums) // 2]

    # Time Complexity: O(n log n), where n is the length of the input array nums.
    # This is because sorting the array takes O(n log n) time.
    #
    # Space Complexity: O(1), as we sort the array in place, modifying the original array.


nums = [2, 2, 1, 1, 1, 2, 2]
# Output: 2

print(majorityElement1(nums))
print(majorityElement2(nums))
print(majorityElement3(nums))
print(majorityElement4(nums))
