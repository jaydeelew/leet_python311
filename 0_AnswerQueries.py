# O. Answering Queries
# Given an integer array nums, an array queries where queries[i] = [x, y] and an integer limit,
# return a boolean array that represents the answer to each query.
# A query is true if the sum of the subarray from x to y is less than limit, or false otherwise.

# This line added for testing purposes.


def answerQueries(nums, queries, limit):
    # build a prefix sum
    prefix = [nums[0]]
    for i in range(1, len(nums)):
        prefix.append(nums[i] + prefix[-1])

    ans = []
    for x, y in queries:
        # Calculate the sum of the subarray from x to y
        # If x is 0, we just take prefix[y]
        # Otherwise, we subtract prefix[x-1] to get the slice sum
        curr = prefix[y] if x == 0 else prefix[y] - prefix[x - 1]
        ans.append(curr < limit)

    return ans


limit = 13
nums = [1, 6, 3, 2, 7, 2]
queries = [[0, 3], [2, 5], [2, 4]]
# Output: [True, False, True]

print(answerQueries(nums, queries, limit))
