# 933. Implement the RecentCounter class. It should support ping(int t),
# which records a call at time t, and then returns an integer representing the number of calls that have happened
# in the range [t - 3000, t]. Calls to ping will have increasing t.

from collections import deque


class RecentCounter:
    def __init__(self):
        self.queue = deque()

    def ping(self, t: int) -> int:
        while self.queue and self.queue[0] < t - 3000:
            self.queue.popleft()

        self.queue.append(t)
        return len(self.queue)


obj = RecentCounter()
calls = [1, 100, 3001, 4000]
for i in calls:
    print(obj.ping(i))
# Output: 1 2 3 2
