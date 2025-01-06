# 2126. Destroying Asteroids
# You are given an integer array asteroids and an integer mass representing the mass of a planet.
# The planet will collide with the asteroids one by one - you can choose the order.
# If the mass of the planet is less than the mass of an asteroid, the planet is destroyed.
# Otherwise, the planet gains the mass of the asteroid. Can you destroy all the asteroids?


class Solution:
    def asteroidsDestroyed(self, mass: int, asteroids: list[int]) -> bool:
        asteroids.sort()
        for asteroid in asteroids:
            if asteroid > mass:
                return False
            mass += asteroid

        return True


mass = 10
asteroids = [3, 9, 19, 5, 21]
# Output: true

sol = Solution()
print(sol.asteroidsDestroyed(mass, asteroids))
