class Solution:
    def is_valid_parenthesis_chars(self, s: str) -> bool:
        stack = []
        matching = {"(": ")", "[": "]", "{": "}"}
        closing = (")", "]", "}")

        for c in s:
            if c in matching:  # if c is an opening bracket
                stack.append(c)
            elif c not in closing:  # if c is not a closing bracket
                continue
            else:  # if c is a closing bracket
                if not stack:
                    return False
                previous_opening = stack.pop()
                if matching[previous_opening] != c:
                    return False
        return not stack


s = "([hello]){world}"  # return True
# s = "([hello]){world})"  # return False
sol = Solution()
print(sol.is_valid_parenthesis_chars(s))
