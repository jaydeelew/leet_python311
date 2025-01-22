# 875. Koko Eating Bananas
# Koko loves to eat bananas. There are n piles of bananas, the ith
# pile has piles[i] bananas. Koko can decide her bananas-per-hour eating speed of k. Each hour,
# she chooses a pile and eats k bananas from that pile.
# If the pile has less than k bananas, she eats all of them and will not eat any more bananas during the hour.
# Return the minimum integer k such that she can eat all the bananas within h hours.
import math


class Solution:
    # piles does not need to be sorted since we are not finding the mid of piles,
    # but the mid of current left and right eating rates
    def minEatingSpeed(self, piles: list[int], h: int) -> int:
        def check(k):
            hours = 0
            for pile_qty in piles:
                # hours it takes to eat this pile at rate of k bananas per hour
                # with any remaining partial piles taking an hour to eat (hence taking the ceiling)
                hours += math.ceil(pile_qty / k)
            # return true if total hours for all piles is <= h
            return hours <= h

        # eating rate must be greater than zero
        left = 1
        # eating rate never needs to exceed the qty of the largest pile per hour
        # since we are looking for the least eating rate
        right = max(piles)
        while left <= right:
            mid = (left + right) // 2
            # if at this rate all piles can be eaten in h hours
            if check(mid):
                right = mid - 1
            else:
                left = mid + 1
        # minimum rate to eat all bananas in h hours
        return left


# piles = [3, 6, 7, 11]
# h = 8
# # Output: 4

# # piles = [30, 11, 23, 4, 20]
# h = 5
# # Output: 30

piles = [30, 11, 23, 4, 20]
h = 6
# Output: 23

sol = Solution()
print(sol.minEatingSpeed(piles, h))
