# Given a string s, find the length of the longest substring without repeating characters.

from collections import defaultdict


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = right = 0
        max_substring = 0
        substring_dic = defaultdict(int)
        for right in range(len(s)):
            right_key = s[right]
            substring_dic[right_key] += 1
            while substring_dic[right_key] > 1:  # while there are repeating characters in subarray/substring
                left_key = s[left]
                substring_dic[left_key] -= 1
                left += 1
            max_substring = max(max_substring, right - left + 1)
            right += 1

        return max_substring


s = "abcabcbb"  # returns 3
# s = "bbbbb"  # returns 1
# s = "pwwkew"  # returns 3
# s = ""  # returns 0
sol = Solution()
print(sol.lengthOfLongestSubstring(s))
