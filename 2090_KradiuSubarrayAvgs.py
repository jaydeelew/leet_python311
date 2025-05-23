# 2090. K Radius Subarray Averages
# You are given a 0-indexed array nums of n integers, and an integer k.
# The k-radius average for a subarray of nums centered at some index i with the radius k
# is the average of all elements in nums between the indices i - k and i + k (inclusive).
# If there are less than k elements before or after the index i, then the k-radius average is -1.
# Build and return an array avgs of length n where avgs[i] is the k-radius average for the subarray centered at index i.
# The average of x elements is the sum of the x elements divided by x, using integer division.
# The integer division truncates toward zero, which means losing its fractional part.


def getAverages(nums: list[int], k: int) -> list[int]:
    prefix = []
    prefix.append(nums[0])
    for i in range(1, len(nums)):
        prefix.append(nums[i] + prefix[-1])

    avgs = []
    for i in range(len(prefix)):
        if i - k < 0 or i + k > len(prefix) - 1:
            avgs.append(-1)
        else:
            kSum = prefix[i + k] - prefix[i - k] + nums[i - k]
            kAvg = kSum // (2 * k + 1)
            avgs.append(kAvg)
    return avgs


nums = [7, 4, 3, 9, 1, 8, 5, 2, 6]
k = 3
# Output: [-1,-1,-1,5,4,4,-1,-1,-1]

# sol = Solution()
print(getAverages(nums, k))
