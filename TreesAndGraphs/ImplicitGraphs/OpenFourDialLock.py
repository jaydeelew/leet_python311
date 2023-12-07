# 752. Open the Lock
# You have a lock with 4 circular wheels. Each wheel has the digits 0 to 9.
# The wheels rotate and wrap around - so 0 can turn to 9 and 9 can turn to 0. Initially,
# the lock reads "0000". One move consists of turning a wheel one slot.
# You are given an array of blocked codes deadends - if the lock reads any of these codes,
# then it can no longer turn. Return the minimum number of moves to make the lock read target.
from collections import deque


class Solution:
    def openLock(self, deadends: list[str], target: str) -> int:
        def neighbors(node: str) -> list[str]:
            ans = []
            for i in range(4):
                # dealing with ith character in string node converted to num
                num = int(node[i])
                # one step for a dial is one up or one down
                for change in [-1, 1]:
                    # for the dial to wrap: e.g. -1 % 10 = 9; 10 % 10 = 0
                    x = (num + change) % 10
                    # slicing: string[start:stop] up to but not including start index, include stop index to end of string
                    # x - 1 & x + 1 are substituted for ith character in string node
                    # "up to index i exclusive" + "x" + "after i to the end"
                    ans.append(node[:i] + str(x) + node[i + 1 :])  # noqa

            return ans

        if "0000" in deadends:
            return -1

        queue = deque([("1234", 0)])  # (node, steps)
        # place deadends in seen to avoid additional "if not deadend" check
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


deadends = ["0201", "0101", "0102", "1212", "2002"]
target = "0202"
# Output: 6

# deadends = ["8888"]
# target = "0009"
# # Output: 1

# deadends = ["8887","8889","8878","8898","8788","8988","7888","9888"]
# target = "8888"
# # Output: -1

sol = Solution()
print(sol.openLock(deadends, target))
