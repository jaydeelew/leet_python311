# Given a string s, reverse the order of characters in each word within a sentence
# while still preserving whitespace and initial word order.


class Solution:
    def reverseWords(self, s: str) -> str:
        # split string into list of strings
        strList = s.split()
        # list to hold reversed words
        rwords = []
        for word in strList:
            # reverse word
            word = word[::-1]
            rwords.append(word)
        # make string from list with elements separated by space
        return " ".join(rwords)


sol = Solution()

s = "there is a new dog in town"
# Output: ereht si a wen god ni nwot

print(sol.reverseWords(s))
