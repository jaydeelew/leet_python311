# Example 1: 739. Daily Temperatures

# Given an array of integers called temperatures that represents the daily temperatures,
# return an array answer such that answer[i] is the number of days you have to wait after the ith day
# to get a warmer temperature. If there is no future day that is warmer, have answer[i] = 0 instead.


class Solution:
    def dailyTemperatures(self, temperatures: list[int]) -> list[int]:
        stack = []
        answer = [0] * len(temperatures)
        for i in range(len(temperatures)):
            while stack and temperatures[i] > temperatures[stack[-1]]:
                j = stack.pop()
                answer[j] = i - j
            stack.append(i)
        return answer


temperatures = [40, 35, 32, 37, 50]  # answer = [4, 2, 1, 1, 0]
sol = Solution()
print(sol.dailyTemperatures(temperatures))
