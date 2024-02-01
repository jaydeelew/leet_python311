# 22. Generate Parentheses
# Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.


class Solution:
    def generateParenthesis(self, n: int) -> list[str]:
        def backtrack(curr_path: list[str], num_open: int, num_close: int):
            if len(curr_path) == n * 2 and curr_path[-1] == "(":
                return

            if num_open > n or num_close > n:
                return

            if num_open < num_close:
                return

            if len(curr_path) == n * 2:
                ans_list.append(curr_path[:])
                return

            parentheses = [")", "("]
            for i in range(len(parentheses)):
                if parentheses[i] == "(":
                    num_open += 1
                else:
                    num_close += 1

                curr_path.append(parentheses[i])
                backtrack(curr_path, num_open, num_close)
                p = curr_path.pop()
                if p == "(":
                    num_open -= 1
                else:
                    num_close -= 1

        ans_list = []
        backtrack(["("], 1, 0)

        output = []
        for str_list in ans_list:
            strg = ""
            for letter in str_list:
                strg += letter
            output.append(strg)

        return output


n = 3
# Output: ["((()))","(()())","(())()","()(())","()()()"]

# n = 2
# Output: ["(())", "()()"]

# n = 1
# Output: ["()"]

sol = Solution()
print(sol.generateParenthesis(n))
