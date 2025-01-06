# 739. Daily Temperatures
# Given an array of integers temperatures represents the daily temperatures,
# return an array answer such that answer[i] is the number of days you have to wait
# after the ith day to get a warmer temperature.
# If there is no future day for which this is possible, keep answer[i] == 0 instead.


def dailyTemperatures_NAIVE(temps):
    ans = [0] * len(temps)

    for i in range(len(temps)):
        j = i + 1
        while j < len(temps):
            if temps[j] > temps[i]:
                ans[i] = j - i
                break
            j += 1

    return ans


def dailyTemperatures(temps):
    ans = [0] * len(temps)
    stack = []

    for curr_index, temp in enumerate(temps):
        while stack and temps[stack[-1]] < temp:
            prev_index = stack.pop()
            ans[prev_index] = curr_index - prev_index
        stack.append(curr_index)

    return ans


temperatures = [73, 74, 75, 71, 69, 72, 76, 73]
# Output: [1,1,4,2,1,1,0,0]

# temperatures = [30,40,50,60]
# Output: [1,1,1,0]

# temperatures = [30,60,90]
# Output: [1,1,0]

print(dailyTemperatures(temperatures))
