# 1870. Minimum Speed to Arrive on Time
# You are given a float hour, representing the amount of time you have to reach the office.
# To commute to the office, you must take n trains in sequential order.
# You are also given an integer array dist, where dist[i] describes the distance of the ith train ride.
# Each train can only depart at an integer hour, so you may need to wait in between each train ride.
# For example, if the 1st train ride takes 1.5 hours, you must wait for an additional 0.5 hours before
# you can depart on the 2nd train ride at the 2-hour mark.
# Return the minimum positive integer speed that all the trains must travel at for you to reach the office
# on time or -1 if it is impossible to be on time. The answer will not exceed 10^7.
import math


class Solution:
    def minSpeedOnTime(self, dist: list[int], hour: float) -> int:
        # since each train must depart on the hour, the minimum total time (the hour parameter)
        # needs to be greater or equal to the number of trains
        if len(dist) > math.ceil(hour):
            return -1

        def check(k):
            t = 0
            for d in dist:
                # round up if train arives at destination before the hour
                t = math.ceil(t)
                # time is distance/speed
                t += d / k
            # if total time taken at speed k is <= hour (amount of time to reach the office)
            return t <= hour

        left = 1
        right = 10**7  # arbitrary top speed
        while left <= right:
            mid = (left + right) // 2
            # check if this speed will make it to the office on time
            if check(mid):
                # if check passes, then all speeds greater than mid are also possible,
                # so we no longer need to check this solution space
                right = mid - 1
            else:
                # if check does not pass, then all speeds less than mid are impossible,
                # so we no longer need to check this solution space
                left = mid + 1
        # return minimum speed
        return left


# dist = [1, 3, 2]
# hour = 6
# # Output: 1

dist = [1, 3, 2]
hour = 2.7
# Output: 3

# dist = [1, 3, 2]
# hour = 1.9
# # Output: -1

sol = Solution()
print(sol.minSpeedOnTime(dist, hour))
