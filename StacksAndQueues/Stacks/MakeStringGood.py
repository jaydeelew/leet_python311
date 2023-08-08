class Solution:
    def make_string_good(self, s):
        stack = []
        for c in s:
            if stack and stack[-1].lower() == c.lower() and stack[-1].islower() != c.islower():
                stack.pop()
            else:
                stack.append(c)
        return "".join(stack)


sol = Solution()
s = "leEeetcode"
# s = "abBAcC"
# s = "s"
print(sol.make_string_good(s))
