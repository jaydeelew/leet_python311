# 1832. A pangram is a sentence where every letter of the English alphabet appears at least once.
# Given a string sentence containing only lowercase English letters, return true if sentence is a pangram, or false otherwise.


class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        seen = set(sentence)
        return True if len(seen) == 26 else False


sentence = "thequickbrownfoxjumpsoverthelazydog"
# Output: True

sol = Solution()
print(sol.checkIfPangram(sentence))
