# 844. Given two strings s and t, return true if they are equal when both are typed into empty text editors.
# '#' means a backspace character.
# For example, given s = "ab#c" and t = "ad#c", return true. Because of the backspace, the strings are both equal to "ac".


class Solution:
    def backspace_string_compare(self, s: str, t: str) -> bool:
        def build(s):
            stack = []
            for c in s:
                if c != "#":
                    stack.append(c)
                elif stack:
                    stack.pop()

            return "".join(stack)

        return build(s) == build(t)


s, t = "ab#c", "af#c"  # returns True
# s, t = "ab##", "c#d#"  # returns True
# s, t = "a#c", "b"  # returns False

sol = Solution()
print(sol.backspace_string_compare(s, t))
