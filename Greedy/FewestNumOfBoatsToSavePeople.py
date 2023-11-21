# 881. Boats to Save People
# You are given an array people where people[i] is the weight of the ith person.
# A boat can hold up to two people, if their weight combined is less than or equal to limit.
# What is the fewest number of boats you need to carry everyone? Note: no person is heavier than limit.


class Solution:
    def numRescueBoats(self, people: list[int], limit: int) -> int:
        ans = 0
        # using two pointers
        l = 0  # lightest person pointer
        h = len(people) - 1  # heaviest person pointer
        people.sort()  # sort ascending in-place

        while l <= h:
            # lightest preson will join heaviest if together not greater than limit
            if people[l] + people[h] <= limit:
                l += 1
            # the heaviest person will always increment answer
            h -= 1
            ans += 1

        return ans


# people = [1, 2]
# limit = 3
# # Output: 1

# people = [3, 2, 2, 1]
# limit = 3
# # Output: 3

# people = [3, 5, 3, 4]
# limit = 5
# # Output: 4

# people = [3, 8, 7, 1, 4]
# limit = 9
# # Output: 3

people = [2, 4]
limit = 5
# Output: 2

sol = Solution()
print(sol.numRescueBoats(people, limit))
