# 1167. You have some number of sticks with positive integer lengths.
# These lengths are given as an array sticks, where sticks[i] is the length of the ith stick.
# You can connect any two sticks of lengths x and y into one stick by paying a cost of x + y.
# You must connect all the sticks until there is only one stick remaining.
# Return the minimum cost of connecting all the given sticks into one stick in this way.
import heapq


def connectSticks(sticks: list[int]) -> int:
    heapq.heapify(sticks)
    len_sticks = len(sticks)
    cost = 0

    # length of sticks minus one to leave one stick remaining
    for _ in range(len_sticks - 1):
        new_stick = heapq.heappop(sticks) + heapq.heappop(sticks)
        cost += new_stick
        heapq.heappush(sticks, new_stick)

    return cost


sticks = [1, 8, 3, 5]
# Output: 30

print(connectSticks(sticks))
