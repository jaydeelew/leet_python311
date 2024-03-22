import time
from collections import defaultdict


class TimerError(Exception):
    """A custom exception used to report errors in use of Timer class"""


class Timer:
    timers = defaultdict(list)

    def __init__(self, precision=8):
        self._start_time = None
        # self.task = None
        self.precision = precision

    def start(self, task="this run"):
        self.task = task
        # accumulated time
        self.timers[task].append(0.0)
        # number of runs
        self.timers[task].append(0)
        """Start a new timer"""
        if self._start_time is not None:
            raise TimerError("Timer is running. Use .stop() to stop it")

        self._start_time = time.perf_counter()

    def stop(self):
        """Stop the timer, and report the elapsed time"""
        global timers
        if self._start_time is None:
            raise TimerError("Timer is not running. Use .start() to start it")

        elapsed_time = time.perf_counter() - self._start_time
        # update acummulative time for each run
        self.timers[self.task][0] += elapsed_time
        # update number of runs
        self.timers[self.task][1] += 1
        self._start_time = None
        print(f"\n{elapsed_time:0.{self.precision}f} seconds for {self.task}")

        avg_time = self.timers[self.task][0] / self.timers[self.task][1]
        print(f"average time: {avg_time:0.{self.precision}f} seconds for {self.timers[self.task][1]} run(s)\n")
