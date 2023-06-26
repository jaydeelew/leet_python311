# Example 1: You are given a string s and an integer k.
# Find the length of the longest substring that contains at most k distinct characters.

# For example, given s = "eceba" and k = 2, return 3. The longest substring with at most 2 distinct characters is "ece".


class Solution:
    def longestsubstringMostKsameChars(self, s: str, k: int) -> int:
        counts = {}
        left = longest = 0
        for right in range(len(s)):
            counts[s[right]] = (
                counts.get(s[right], 0) + 1
            )  # if dictionary entry does not exist, assign 0, else assign current character from s
            while len(counts) > k:  # if dictionary length is longer than k
                del counts[s[left]]  # delete left entry of current window/subarray
                left += 1
            # longest = max(longest, sum(dic.values()))
            longest = max(longest, right - left + 1)  # right - left + 1 is length of current subarray
        return longest


"""
        # Using Default Dictionary #
        counts = defaultdict(int)
        left = longest = 0
        for right in range(len(s)):
            counts[s[right]] += 1
            while len(counts) > k:
                counts[s[left]] -= 1
                if counts[s[left]] == 0:
                    del counts[s[left]]
                left += 1
            longest = max(ans, right - left + 1)
        return longest
"""

s = "eceba"
k = 2
sol = Solution()
print(sol.longestsubstringMostKsameChars(s, k))
