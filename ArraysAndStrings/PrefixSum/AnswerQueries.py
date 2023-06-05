# Example 1: Given an integer array nums, an array queries where queries[i] = [x, y] and an integer limit,
# return a boolean array that represents the answer to each query.
# A query is true if the sum of the subarray from x to y is less than limit, or false otherwise.

# For example, given nums = [1, 6, 3, 2, 7, 2] and queries = [[0, 3], [2, 5], [2, 4]] and limit = 13,
# the answer is [true, false, true]. For each query, the subarray sums are [12, 14, 12].


def answer_queries(nums, queries, limit) -> list:
    # build a prefix sum
    prefix = [nums[0]]  # create an array named prefix with its first element the same as first element from nums
    for i in range(1, len(nums)):  # since zeroeth element already added to prefix, begin iterating at index 1
        prefix.append(nums[i] + prefix[-1])  # add to end of prefix current value from nums plus last value in prefix

    ans = []  # create answer array to append to
    for x, y in queries:  # iterate through a list of tuples representing range in nums subarray
        curr = (
            prefix[y] - prefix[x] + nums[x]
        )  # this will provide the sum of the query-subarray in nums in O(1) time instead of O(range provided)
        ans.append(curr < limit)  # if sum of current nums subarray range is less than provided limit, true, else false

    return ans


limit = 13
nums = [1, 6, 3, 2, 7, 2]
# prefix [1, 7, 10, 12, 19, 21] - this is calclulated by the method
queries = [[0, 3], [2, 5], [2, 4]]

print(answer_queries(nums, queries, limit))
