# 771. You're given strings jewels representing the types of stones that are jewels,
# and stones representing the stones you have. Each character in stones is a type of stone you have.
# You want to know how many of the stones you have are also jewels.
# Letters are case sensitive, so "a" is considered a different type of stone from "A"

from collections import Counter


class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        stones_count = Counter(stones)
        qty = 0
        for j in jewels:
            qty += stones_count[j]

        return qty


jewels = "aA"
stones = "gggAYbbabb"
# Output: 2

sol = Solution()
print(sol.numJewelsInStones(jewels, stones))
