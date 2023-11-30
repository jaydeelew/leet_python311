# 2300. Successful Pairs of Spells and Potions
# You are given two positive integer arrays spells and potions, of length n and m respectively,
# where spells[i] represents the strength of the ith spell and potions[j] represents the strength of the jth potion.
# You are also given an integer success.
# A spell and potion pair is considered successful if the product of their strengths is at least success.
# Return an integer array pairs of length n where pairs[i] is the number of potions
# that will form a successful pair with the ith spell.


class Solution:
    def successfulPairs(self, spells: list[int], potions: list[int], success: int) -> list[int]:
        def binary_search(arr: list[int], target: int):
            left = 0
            right = len(arr) - 1

            while left <= right:
                mid = (left + right) // 2
                if target <= arr[mid]:
                    right = mid - 1
                else:
                    left = mid + 1

            return left

        # arrays for binary search must be sorted
        potions.sort()
        ans = []
        for spell in spells:
            target = success / spell
            index = binary_search(potions, target)
            ans.append(len(potions) - index)

        return ans


# spells = [5, 1, 3]
# potions = [1, 2, 3, 4, 5]
# success = 7
# # Output: [4,0,3]

spells = [3, 1, 2]
potions = [8, 5, 8]
success = 16
Output: [2, 0, 2]

sol = Solution()
print(sol.successfulPairs(spells, potions, success))
