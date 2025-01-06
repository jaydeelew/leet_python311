# 1004. Given a binary array nums and an integer k,
# return the maximum number of consecutive 1's in the array if you can flip at most k 0's


def longestOnes(nums: list[int], k: int) -> int:
    left = flips = curlen = maxlen = 0
    # make an actual copy of array instead of a reference to same array (i.e. arr = nums)
    arr = nums.copy()
    for right in range(0, len(nums)):
        # increase current length of "consecutive ones" subarray each iteration
        curlen += 1
        # if this iteration encounters a zero
        if arr[right] == 0:
            # change zero to a one
            arr[right] = 1
            # increase amount of flips by one
            flips += 1
            # if flips exceed k
            if flips == k + 1:
                # move left window boundary until it passes a zero
                while nums[left] == 1:
                    # once nums[left] hits a zero, the loop will terminate
                    left += 1
                    # reduce current length by one
                    curlen -= 1
                # move left window boundary past zero
                left += 1
                # reduce current length by one
                curlen -= 1
                # reduce flips by one to return to max number of flips
                flips -= 1
        if curlen > maxlen:
            maxlen = curlen
    return maxlen


# k = 3
# nums = [0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 1, 1, 0, 0, 0, 1, 1, 1, 1]
# # Output: 10

# k = 2
# nums = [1, 0, 1, 1, 0, 0, 1, 1, 1, 0, 1]
# # Output: 7

k = 2
nums = [1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 0]
# Output: 6

print(longestOnes(nums, k))
