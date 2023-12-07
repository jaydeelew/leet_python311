# 399. Evaluate Division
# You are given an array equations and a number array values of the same length.
# equations[i] = [x, y] represents x / y = values[i]. You are also given an array queries where queries[i] = [a, b]
# which represents the quotient a / b. Return an array answer where answer[i] is the answer to the ith query,
# or -1 if it cannot be determined.

from collections import defaultdict


class Solution:
    def calcEquation(self, equations: list[list[str]], values: list[float], queries: list[list[str]]) -> list[float]:
        def answer_query(start, end):
            # start is a numerator from queries looking for same numerator or denominator in graph
            if start not in graph:
                return -1

            # seen numerators in queries list
            seen = {start}
            # (numerator as string from queries, edge multiplier thus far to this node... aka ratio)
            stack = [(start, 1)]

            while stack:
                node, ratio = stack.pop()
                # if denominator is found as
                if node == end:
                    return ratio

                # since graph is dict of dicts, neighbors are keys of each inner dict
                for neighbor in graph[node]:
                    if neighbor not in seen:
                        seen.add(neighbor)
                        # (neighbor, current ratio thus far * neighbors' ratio thus far)
                        # instead of steps, we calc current ratio
                        stack.append((neighbor, ratio * graph[node][neighbor]))

            return -1

        # build graph using dict of numerator and denominator keys w/ values as dict entries with keys as corresponing
        # numerator/denominator and values as the edge multiplier between them.
        graph = defaultdict(dict)  # a dict of dict because strings are used as keys in each dict
        for i in range(len(equations)):
            numerator, denominator = equations[i]
            val = values[i]
            graph[numerator][denominator] = val
            graph[denominator][numerator] = 1 / val

        ans = []  # list of ratios from queries processed through answer_query
        for numerator, denominator in queries:
            ans.append(answer_query(numerator, denominator))

        return ans


equations = [["a", "b"], ["b", "c"]]
values = [2.0, 3.0]
queries = [["a", "c"], ["b", "a"], ["a", "e"], ["a", "a"], ["x", "x"]]
# Output: [6.00000,0.50000,-1.00000,1.00000,-1.00000]

# equations = [["a", "b"], ["b", "c"], ["bc", "cd"]]
# values = [1.5, 2.5, 5.0]
# queries = [["a", "c"], ["c", "b"], ["bc", "cd"], ["cd", "bc"]]
# # Output: [3.75000,0.40000,5.00000,0.20000]

# equations = [["a","b"]]
# values = [0.5]
# queries = [["a","b"],["b","a"],["a","c"],["x","y"]]
# # Output: [0.50000,2.00000,-1.00000,-1.00000]

sol = Solution()
print(sol.calcEquation(equations, values, queries))
