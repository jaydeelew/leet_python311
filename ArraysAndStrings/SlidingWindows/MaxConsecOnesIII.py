# Given a binary array nums and an integer k,
# return the maximum number of consecutive 1's in the array if you can flip at most k 0's


def longestOnes(nums, k) -> int:
    left = flips = curlen = maxlen = 0
    arr = nums.copy()  # a way to make an actual copy of array instead of a reference to same array (arr = nums)
    for right in range(0, len(nums)):
        curlen += 1  # increase current length of "consecutive ones" subarray each iteration
        if arr[right] == 0:  # if this iteration encounters a zero
            arr[right] = 1  # change zero to a one
            flips += 1  # increase amount of flips by one
            if flips == k + 1:  # if flips exceed k
                while nums[left] == 1:  # move left window boundary until it passes a zero
                    left += 1  # once nums[left] hits a zero, the loop will terminate
                    curlen -= 1  # reduce current length by one
                left += 1  # move left window boundary past zero
                curlen -= 1  # reduce current length by one
                flips -= 1  # reduce flips by one to return to max number of flips
        if curlen > maxlen:
            maxlen = curlen
    return maxlen


k = 3
# nums = [1,0,1,1,0,0,1,1,1,0,1] # 7 if k = 2
# nums = [1,1,1,0,0,0,1,1,1,1,0] # 6 if k = 2
nums = [0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 1, 1, 0, 0, 0, 1, 1, 1, 1]  # 10 if k = 3
print(longestOnes(nums, k))
