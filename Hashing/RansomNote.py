# 383. Given two strings ransomNote and magazine, return true if ransomNote can be constructed
# by using the letters from magazine and false otherwise.
# Each letter in magazine can only be used once in ransomNote.from collections import Counter
from collections import Counter


class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        # Alternative Solution:
        # magazine_counts = Counter(magazine)
        # ransom_counts = Counter(ransomNote)
        # for key in ransom_counts:
        #     if ransom_counts[key] > magazine_counts[key]:
        #         return False
        # return True

        magazine_counts = Counter(magazine)
        for c in ransomNote:
            magazine_counts[c] -= 1
            if magazine_counts[c] < 0:
                return False
        return True


ransomNote = "acabbaa"
magazine = "aabaa"
# Output: False

sol = Solution()
print(sol.canConstruct(ransomNote, magazine))
