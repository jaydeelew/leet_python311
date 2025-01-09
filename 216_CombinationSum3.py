# 216. Combination Sum III
# Find all valid combinations of k numbers that sum up to n such that the following conditions are true:
# - Only numbers 1 through 9 are used.
# - Each number is used at most once.
# Return a list of all possible valid combinations. The list must not contain the same combination twice,
# and the combinations may be returned in any order.


class Solution:
    def combinationSum3(self, k: int, n: int) -> list[list[int]]:
        output = []

        def backtrack(curr_list: list[int], curr_num, curr_sum):
            if curr_sum == n and len(curr_list) == k:
                # always append copy of current list and not a reference to it
                output.append(curr_list[:])
                return

            for i in range(curr_num, 10):
                if curr_sum + i <= n:
                    curr_list.append(i)
                    backtrack(curr_list, i + 1, sum(curr_list))
                    curr_list.pop()

        backtrack([], 1, 0)
        return output


# k = 3
# n = 7
# Output: [[1,2,4]]

k = 3
n = 9
# Output: [[1,2,6],[1,3,5],[2,3,4]]

sol = Solution()
print(sol.combinationSum3(k, n))
