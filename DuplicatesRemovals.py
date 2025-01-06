# 1047. You are given a string s.
# Continuously remove duplicates (two of the same character beside each other) until you can't anymore.
# Return the final string after this.
# For example, given s = "abbaca", you can first remove the "bb" to get "aaca". Next, you can remove the "aa" to get "ca".
# "ca" is the final answer.


class Solution:
    def duplicates_removal(self, s):
        stack = []
        for c in s:
            if stack and stack[-1] == c:
                stack.pop()
            else:
                stack.append(c)
        return "".join(stack)


s = "abbaca"  # return "ca"
# s = "azxxzy"  # return "ay"

sol = Solution()
print(sol.duplicates_removal(s))
