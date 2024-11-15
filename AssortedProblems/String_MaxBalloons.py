from collections import Counter


class Solution:
    def maxNumberOfBalloons(self, text):
        balloon = "balloon"
        counts = Counter(text)

        if any(c not in counts for c in balloon):
            return 0
        else:
            return min(counts["b"], counts["a"], counts["l"] // 2, counts["o"] // 2, counts["n"])


str = "nlaebolko"
sol = Solution()
print(sol.maxNumberOfBalloons(str))
