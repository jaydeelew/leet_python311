# Example 1: 49. Group Anagrams
# Given an array of strings strs, group the anagrams together.

# For example, given strs = ["eat","tea","tan","ate","nat","bat"], return [["bat"],["nat","tan"],["ate","eat","tea"]].

from collections import defaultdict


class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        anagramGroups = defaultdict(list)
        for anagram in strs:  # O(n: length of strs)
            key = "".join(sorted(anagram))  # O(m: avg length of string) * O(log m: sort) - sort each anagram to find key
            anagramGroups[key].append(anagram)  # O(1) - append unsorted anagram to anagramGroups by key

        return list(anagramGroups.values())


strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
sol = Solution()
print(sol.groupAnagrams(strs))  # output: [["bat"],["nat","tan"],["ate","eat","tea"]]

# time complexity: O(n * m * log m) - for each list in strs * sorting lists of avg size m
# space complexity: O(n * m) - anagrams of average size m placed in n keys
