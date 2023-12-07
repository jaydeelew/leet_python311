# Given a string s, return the first character to appear twice.
# It is guaranteed that the input will have a duplicate character.


class Solution:
    def repeatedCharacter(self, s: str) -> str:
        myset = set()
        for i in s:
            if i in myset:
                return i
            myset.add(i)


s = "abcdeda"
sol = Solution()
# Output: d

print(sol.repeatedCharacter(s))
