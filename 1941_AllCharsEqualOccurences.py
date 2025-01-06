# 1941. Check if All Characters Have Equal Number of Occurrences
# Given a string s, determine if all characters have the same frequency.
# For example, given s = "abacbc", return true. All characters appear twice.
# Given s = "aaabb", return false. "a" appears 3 times, "b" appears 2 times. 3 != 2.

from collections import Counter


class Solution:
    def areOccurrencesEqual(self, s: str) -> bool:
        counts_of_frequencies = Counter(s)
        # frequencies is type: dict_values
        frequencies = counts_of_frequencies.values()
        # create set from frequencies, if length is one, then all frequency counts are equal
        return len(set(frequencies)) == 1


s = "ablacbcl"
sol = Solution()
# Output: True

print(sol.areOccurrencesEqual(s))
