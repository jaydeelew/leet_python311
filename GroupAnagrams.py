# 49. Group Anagrams
# Given an array of strings strs, group the anagrams together.


from collections import defaultdict


class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        anagramGroups = defaultdict(list)
        for anagram in strs:
            key = "".join(sorted(anagram))
            anagramGroups[key].append(anagram)

        return list(anagramGroups.values())


strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
sol = Solution()
print(sol.groupAnagrams(strs))  # output: [["bat"],["nat","tan"],["ate","eat","tea"]]

# time complexity: O(n * m * log m) - for each list in strs * sorting lists of avg size m
# space complexity: O(n * m) - anagrams of average size m placed in n keys
