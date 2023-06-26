from collections import Counter


class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
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
sol = Solution()
print(sol.canConstruct(ransomNote, magazine))
