class Solution:
    def letter_combos(self, letters: list[str], k: int) -> list[list[str]]:
        def backtrack(curr):
            if len(curr) == k:
                ans.append(curr.copy())
                return

            for ltr in letters:
                if ltr not in curr:
                    curr.append(ltr)
                    backtrack(curr)
                    curr.pop()

        ans = []
        backtrack([])
        return ans


letters = ["b", "a", "t"]
k = 2
# Output: [['b', 'a'], ['b', 't'], ['a', 'b'], ['a', 't'], ['t', 'b'], ['t', 'a']]
sol = Solution()
print(sol.letter_combos(letters, k))
