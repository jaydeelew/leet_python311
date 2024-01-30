# 77. Combinations
# Given two integers n and k, return all possible combinations of k numbers chosen from the range [1, n].
# You may return the answer in any order.


class Solution:
    def combine(self, n: int, k: int) -> list[list[int]]:
        def backtrack(curr_path, i):
            if len(curr_path) == k:
                ans.append(curr_path.copy())
                return

            for num in range(i, n + 1):
                curr_path.append(num)
                backtrack(curr_path, num + 1)
                curr_path.pop()

        ans = []
        backtrack([], 1)
        return ans


n = 4
k = 2
# Output: [[1,2],[1,3],[1,4],[2,3],[2,4],[3,4]]

# n = 1
# k = 1
# # Output: [[1]]

sol = Solution()
print(sol.combine(n, k))
