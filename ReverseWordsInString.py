# Given a string s, reverse the order of characters in each word within a sentence
# while still preserving whitespace and initial word order.


class Solution:
    def reverseWords(self, s: str) -> str:
        # make an array of strings from s
        split_str = s.split()
        reversed = []

        for str in split_str:
            # make an array of characters out of a string
            char_arr = list(str)
            left = 0
            right = len(str) - 1

            while left < right:
                char_arr[left], char_arr[right] = char_arr[right], char_arr[left]
                left += 1
                right -= 1
            # make reversed an array of strings
            reversed.append("".join(char_arr))

        # make result one string from an array of strings
        result = " ".join(reversed)
        return result

    # an option to the two-pointers solution
    def reverseWords2(self, s: str) -> str:
        # split string into list of strings
        strList = s.split()
        # list to hold reversed words
        reversed_words = []
        for word in strList:
            # reverse word with slicing [start:stop:step]
            word = word[::-1]
            reversed_words.append(word)
        # make string from list with elements separated by space
        return " ".join(reversed_words)


sol = Solution()

s = "there is a new dog in town"
# Output: ereht si a wen god ni nwot

print(sol.reverseWords(s))
print(sol.reverseWords2(s))
