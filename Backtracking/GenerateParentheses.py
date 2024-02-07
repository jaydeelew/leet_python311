# 22. Generate Parentheses
# Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.


# 1st Solution:
# class Solution:
#     def generateParenthesis(self, n: int) -> list[str]:
#         ans_list = []

#         def backtrack(curr_path: list[str], num_open: int, num_close: int):
#             if len(curr_path) == n * 2 and curr_path[-1] == "(":
#                 return
#             if num_open > n or num_open < num_close:
#                 return
#             if len(curr_path) == n * 2:
#                 ans_list.append("".join(curr_path))
#                 return

#             parentheses = [")", "("]
#             for i in range(len(parentheses)):
#                 if parentheses[i] == "(":
#                     num_open += 1
#                 else:
#                     num_close += 1

#                 curr_path.append(parentheses[i])
#                 backtrack(curr_path, num_open, num_close)
#                 p = curr_path.pop()
#                 if p == "(":
#                     num_open -= 1
#                 else:
#                     num_close -= 1

#         backtrack(["("], 1, 0)
#         return ans_list


class Solution:
    def generateParenthesis(self, n: int) -> list[str]:
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

sol = Solution()
print(sol.generateParenthesis(n))
