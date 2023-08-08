# Given a stream of integers and a window size, calculate the moving average of all integers in the sliding window.
# Implement the MovingAverage class:
# MovingAverage(int size) Initializes the object with the size of the window size.
# double next(int val) Returns the moving average of the last size values of the stream.

from collections import deque


class MovingAverage:
    def __init__(self, size: int):
        self.window_size = size
        self.queue = deque()
        self.moving_sum = 0
        self.moving_avg = 0

    def next(self, val: int) -> float:
        self.queue.append(val)
        self.moving_sum += val
        if len(self.queue) <= self.window_size:
            self.moving_avg = self.moving_sum / len(self.queue)
        else:
            self.moving_sum -= self.queue.popleft()
            self.moving_avg = self.moving_sum / self.window_size
        return self.moving_avg


movingAverage = MovingAverage(3)
print(movingAverage.next(1))  # return 1.0 = 1 / 1
print(movingAverage.next(10))  # return 5.5 = (1 + 10) / 2
print(movingAverage.next(3))  # return 4.66667 = (1 + 10 + 3) / 3
print(movingAverage.next(5))  # return 6.0 = (10 + 3 + 5) / 3
