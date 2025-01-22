# 502. IPO
# LeetCode would like to work on some projects to increase its capital before IPO.
# You are given n projects where the ith project has a profit of profits[i]
# and a minimum capital of capital[i] is needed to start it.
# Initially, you have w capital. When you finish a project, the profit will be added to your total capital.
# Return the max capital possible if you are allowed to do up to k projects.
import heapq


def findMaximizedCapital(k: int, w: int, profits: list[int], capital: list[int]) -> int:
    profsNcapl = sorted(zip(capital, profits))
    totalCapital = w
    maxHeap = []
    # i needs to be outside the nested while loop since it is conditionally incremented
    i = 0
    for _ in range(k):
        while i < len(profsNcapl) and profsNcapl[i][0] <= totalCapital:
            # push on the profit
            heapq.heappush(maxHeap, -profsNcapl[i][1])
            i += 1

        # if there is nothing on the heap, we are out of capital
        if len(maxHeap) == 0:
            return totalCapital

        # since maxHeap pops a negative, we must negate it
        totalCapital -= heapq.heappop(maxHeap)

    return totalCapital


# k = 2
# w = 0
# profits = [1, 2, 3]
# capital = [0, 1, 1]
# Output: 4

# k = 3
# w = 0
# profits = [1, 2, 3]
# capital = [0, 1, 2]
# # Output: 6

k = 3
w = 0
profits = [1, 2, 3]
capital = [1, 1, 2]
# Output: 0

# k = 10
# w = 0
# profits = [1, 2, 3]
# capital = [0, 1, 2]
# # Output: 6

print(findMaximizedCapital(k, w, profits, capital))
