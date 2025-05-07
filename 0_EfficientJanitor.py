# 0. Efficient Janitor
# The janitor of a high school is extremely efficient.
# By the end of each day, all of the school's waste is in plastic bags weighing between 1.01 pounds and 3.00 pounds.
# All plastic bags are then taken to the trash bins outside.
# One trip is described as selecting a number of bags which together do not weigh more than 3.00 pounds,
# dumping them in the outside trash can, and returning to the school.
# Given the number of plastic bags n, and the weights of each bag,
# determine the minimum number of trips the janitor has to make.


def numberOfBags(n: int, weights: list) -> int:
    weights.sort(reverse=True)

    trips = 0
    left = 0
    right = n - 1

    # Use two pointers to try pairing heaviest with lightest bags
    while left <= right:
        # If we're at the last bag or current bag + lightest bag exceeds limit
        if left == right or weights[left] + weights[right] > 3.0:
            trips += 1
            left += 1
        else:
            # We can pair current heaviest with current lightest
            trips += 1
            left += 1
            right -= 1

    return trips


n = 5
weight = [1.01, 1.99, 2.5, 1.5, 1.01]
# Output: 3
# The janitor can carry all plastic bags out in 3 trips:
# [1.01 + 1.99, 2.5, 1.5 + 1.01]

print(numberOfBags(n, weight))
