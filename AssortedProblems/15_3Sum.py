# 15. 3Sum
# Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]]
# such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.
# Notice that the solution set must not contain duplicate triplets.


def threeSum(nums: list[int]) -> list[list[int]]:

    nums.sort()  # O(nlogn)
    ans = []
    for i in range(len(nums)):  # O(n)
        if i > 0 and nums[i] == nums[i - 1]:  # skip duplicates
            continue
        target = 0 - nums[i]
        left = i + 1
        right = len(nums) - 1
        while left < right:  # O(n)
            twosum = nums[left] + nums[right]
            if twosum == target:
                ans.append([nums[i], nums[left], nums[right]])
                left += 1
                right -= 1
                # Skip duplicates for left and right pointers
                while left < right and nums[left] == nums[left - 1]:
                    left += 1
                while left < right and nums[right] == nums[right + 1]:
                    right -= 1
            elif twosum < target:
                left += 1
            elif twosum > target:
                right -= 1

    return ans

    # time complexity O(nlogn + n^2) -> O(n^2)
    # space complexity O(1)


nums = [-1, 0, 1, 2, -1, -4]
# Output: [[-1,-1,2],[-1,0,1]]

# nums = [1, -1, -1, 0, 2]
# Output: [[1, -1, 0], [-1, -1, 2]]

# nums = [0, 0, 0, 0]
# Output: [[0, 0, 0]]

# nums = [-2, 0, 1, 1, 2]
# Output: [[-2,0,2], [-2, 1, 1]]

# nums = [1, 2, -2, -1]
# Output: []

print(threeSum(nums))
