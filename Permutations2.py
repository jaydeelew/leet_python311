class Solution:
    def letter_combos(self, letters: list[str], k: int) -> list[list[str]]:
        def backtrack(curr_path):
            if len(curr_path) == k:
                ans.append(curr_path.copy())
                return

            for ltr in letters:
                if ltr not in curr_path:
                    curr_path.append(ltr)
                    backtrack(curr_path)
                    curr_path.pop()

        ans = []
        backtrack([])
        return ans


letters = ["b", "a", "t"]
k = 2
# Output: [['b', 'a'], ['b', 't'], ['a', 'b'], ['a', 't'], ['t', 'b'], ['t', 'a']]

sol = Solution()
print(sol.letter_combos(letters, k))
