# 340. Longest Substring with At Most K Distinct Characters
# You are given a string s and an integer k.
# Find the length of the longest substring that contains at most k distinct characters.


def longestsubstringMostKsameChars(s: str, k: int) -> int:
    counts = {}
    left = longest = 0
    for right in range(len(s)):
        # if dictionary entry does not exist, assign 0, else assign current character from s
        counts[s[right]] = counts.get(s[right], 0) + 1
        while len(counts) > k:
            # delete left entry of current window/subarray
            del counts[s[left]]
            left += 1
        # right - left + 1 is length of current subarray
        longest = max(longest, right - left + 1)
    return longest

    # Using Default Dictionary
    # counts = defaultdict(int)
    # left = longest = 0
    # for right in range(len(s)):
    #     counts[s[right]] += 1
    #     while len(counts) > k:
    #         counts[s[left]] -= 1
    #         if counts[s[left]] == 0:
    #             del counts[s[left]]
    #         left += 1
    #     longest = max(ans, right - left + 1)
    # return longest


s = "eceba"
k = 2
# Output: 3

print(longestsubstringMostKsameChars(s, k))
