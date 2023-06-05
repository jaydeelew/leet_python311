# Given a string s, reverse the order of characters in each word within a sentence
# while still preserving whitespace and initial word order.


class Solution:
    def reverseWords(self, s: str) -> str:
        strList = s.split()  # split string into list of strings
        rwords = []  # list to hold reversed words
        for word in strList:
            word = word[::-1]  # reverse word
            rwords.append(word)
        return " ".join(rwords)  # make string from list with elements separated by space


sol = Solution()
s = "there is a new dog in town"
print(sol.reverseWords(s))
