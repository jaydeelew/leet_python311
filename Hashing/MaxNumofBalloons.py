# 1189. Given a string text, you want to use the characters of text to form as many instances of the word "balloon" as possible.
# You can use each character in text at most once. Return the maximum number of instances that can be formed.

from collections import Counter


class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        textCounts = Counter(text)
        balloonCounts = Counter("balloon")
        for key in balloonCounts:
            # take floor when dividing textCounts by baloonCounts
            # and 0 when character in baloon does not exist in text
            balloonCounts[key] = textCounts.get(key, 0) // balloonCounts[key]

        # the minimum value in balloonCounts is the max number of times word 'baloon' can be formed
        return min(balloonCounts.values())


text = "balon"  # Output: 0
# text = "nlaebolko" # Output: 1
# text = "loonbalxballpoon" # Output: 2

sol = Solution()
print(sol.maxNumberOfBalloons(text))
