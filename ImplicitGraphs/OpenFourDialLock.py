# 752. Open the Lock
# You have a lock with 4 circular wheels. Each wheel has the digits 0 to 9.
# The wheels rotate and wrap around - so 0 can turn to 9 and 9 can turn to 0. Initially,
# the lock reads "0000". One move consists of turning a wheel one slot.
# You are given an array of blocked codes deadends - if the lock reads any of these codes,
# then it can no longer turn. Return the minimum number of moves to make the lock read target.
from collections import deque


class Solution:
    def openLock(self, deadends: list[str], target: str) -> int:
        def neighbors(node):
            ans = []
            for i in range(4):
                num = int(node[i])
                for change in [-1, 1]:
                    x = (num + change) % 10
                    ans.append(node[:i] + str(x) + node[i + 1 :])

            return ans

        if "0000" in deadends:
            return -1

        queue = deque([("0000", 0)])
        seen = set(deadends)
        seen.add("0000")

        while queue:
            node, steps = queue.popleft()
            if node == target:
                return steps

            for neighbor in neighbors(node):
                if neighbor not in seen:
                    seen.add(neighbor)
                    queue.append((neighbor, steps + 1))

        return -1


sol = Solution()

deadends = ["0201", "0101", "0102", "1212", "2002"]
target = "0202"
# Output: 6

# deadends = ["8888"]
# target = "0009"
# # Output: 1

# deadends = ["8887","8889","8878","8898","8788","8988","7888","9888"]
# target = "8888"
# # Output: -1

print(sol.openLock(deadends, target))
