# 1189. Maximum Number of Balloons
# Given a string text, you want to use the characters of text to form as many instances of the word "balloon" as possible.
# You can use each character in text at most once. Return the maximum number of instances that can be formed.
from collections import Counter


def maxNumberOfBalloons(text):
    balloon = "balloon"
    counts = Counter(text)

    if any(c not in counts for c in balloon):
        return 0
    else:
        return min(counts["b"], counts["a"], counts["l"] // 2, counts["o"] // 2, counts["n"])


str = "nlaebolko"
print(maxNumberOfBalloons(str))
