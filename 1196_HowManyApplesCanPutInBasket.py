# 1196 - How Many Apples Can You Put into the Basket
# You have some apples and a basket that can carry up to 5000 units of weight.
# Given an integer array weight where weight[i] is the weight of the ith apple,]
# return the maximum number of apples you can put in the basket.


def maxNumberOfApples(weight: list[int]) -> int:
    weight.sort()
    capacity = 5000
    apples = 0

    for w in weight:
        if capacity - w >= 0:
            apples += 1
            capacity -= w
            # remaining capacity is zero
            if capacity == 0:
                return apples
        else:
            # remaining capacity is negative
            return apples
    # remaining capacity is positive
    return apples


# weight = [4000, 2000, 3000, 1000]
# # Output: 2

# weight = [100, 200, 150, 1000]
# # Output: 4

weight = [900, 950, 800, 1000, 700, 800]
# Output: 5

print(maxNumberOfApples(weight))
