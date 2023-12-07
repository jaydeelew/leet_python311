# 1426. Given an integer array arr, count how many elements x there are,
# such that x + 1 is also in arr. If there are duplicates in arr, count them separately.


class Solution:
    def countElements(self, arr: list[int]) -> int:
        count = 0
        mySet = arr
        for num in arr:
            if num + 1 in mySet:
                count += 1
        return count


arr = [1, 2, 3]
# Output: 2

# arr = [1,1,3,3,5,5,7,7]
# # Output: 0

sol = Solution()
print(sol.countElements(arr))
