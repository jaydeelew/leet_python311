# 22. Generate Parentheses
# Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.


def generateParenthesis(n: int) -> list[str]:
    answer = []

    def backtracking(cur_string, left_count, right_count):
        if len(cur_string) == 2 * n:
            answer.append("".join(cur_string))
            return
        # must start with opening parenthesis
        # left count will finally equal n
        if left_count < n:
            cur_string.append("(")
            backtracking(cur_string, left_count + 1, right_count)
            cur_string.pop()
        # right count cannot exceed left count
        if right_count < left_count:
            cur_string.append(")")
            backtracking(cur_string, left_count, right_count + 1)
            cur_string.pop()

    backtracking([], 0, 0)
    return answer


n = 3
# Output: ["((()))","(()())","(())()","()(())","()()()"]

# n = 2
# Output: ["(())", "()()"]

# n = 1
# Output: ["()"]

print(generateParenthesis(n))
