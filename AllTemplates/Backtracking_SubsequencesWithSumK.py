# given an array of integers and an integer k, return an array of arrays of all subsequences with sum k
def find_subsequences_with_sum_k(nums, k):
    def backtrack(start_index, curr_path, curr_sum):
        if curr_sum == k:
            ans.append(curr_path[:])
            # since there are no more numbers to add to curr_path, we return
            return

        for i in range(start_index, len(nums)):
            new_sum = curr_sum + nums[i]
            # if the new sum is greater than k, we continue to the next number in the nums array
            if new_sum <= k:
                curr_path.append(nums[i])
                # the starting index is i+1, not i
                # this prevents the same number from being used multiple times
                backtrack(i + 1, curr_path, new_sum)
                curr_path.pop()

    ans = []
    backtrack(0, [], 0)
    return ans


nums = [1, 2, 3, 4, 5]
k = 5
# Output: [[1, 4], [2, 3], [5]]

# nums = [2, 3, 1, 5, 2]
# k = 5
# Output: [[2, 3], [2, 1, 2], [3, 2], [5]]

print(find_subsequences_with_sum_k(nums, k))
