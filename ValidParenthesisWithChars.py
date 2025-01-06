# Not a LeetCode problem as far as I can tell. See problem 20 for the base of this problem.


class Solution:
    def is_valid_parenthesis_chars(self, s: str) -> bool:
        stack = []
        matching = {"(": ")", "[": "]", "{": "}"}
        closing = (")", "]", "}")

        for c in s:
            # if c is an opening bracket
            if c in matching:
                stack.append(c)
            # if c is not a closing bracket
            elif c not in closing:
                continue
            # if c is a closing bracket
            else:
                if not stack:
                    return False
                previous_opening = stack.pop()
                if matching[previous_opening] != c:
                    return False
        return not stack


s = "([hello]){world}"  # Output: True
# s = "([hello]){world})"  # Output: False

sol = Solution()
print(sol.is_valid_parenthesis_chars(s))
