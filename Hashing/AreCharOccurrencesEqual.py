# Example 3: 1941. Check if All Characters Have Equal Number of Occurrences
# Given a string s, determine if all characters have the same frequency.

# For example, given s = "abacbc", return true. All characters appear twice.
# Given s = "aaabb", return false. "a" appears 3 times, "b" appears 2 times. 3 != 2.

from collections import Counter


class Solution:
    def areOccurrencesEqual(self, s: str) -> bool:
        counts_of_frequencies = Counter(s)
        frequencies = counts_of_frequencies.values()  # frequencies is type: dict_values
        return len(set(frequencies)) == 1  # create set from frequencies, if length is one, then all frequency counts are equal


s = "ablacbcl"
sol = Solution()
print(sol.areOccurrencesEqual(s))
