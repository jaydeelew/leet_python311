# 77. Combinations
# Given two integers n and k, return all possible combinations of k numbers chosen from the range [1, n].
# You may return the answer in any order.
# Note that combinations are unordered, i.e., [1,2] and [2,1] are considered to be the same combination.
from itertools import combinations


def combine_1(n, k):
    return list(combinations(range(1, n + 1), k))


def combine_2(n, k):
    # Use iterative approach with binary sorted state
    result = []
    combo = list(range(1, k + 1))  # Start with smallest combination [1,2,3,...,k]

    while True:
        result.append(combo[:])

        # Find the rightmost number that can be incremented
        i = k - 1
        while i >= 0 and combo[i] == n - k + i + 1:
            i -= 1

        # If no number can be incremented, we're done
        if i < 0:
            break

        # Increment the number at i and reset subsequent numbers
        combo[i] += 1
        for j in range(i + 1, k):
            combo[j] = combo[j - 1] + 1

    return result


def combine_3(n, k):
    def bt(si, curr_combo):

        if len(curr_combo) == k:
            ans.append(curr_combo[:])
            return

        for i in range(si, n):
            curr_combo.append(i + 1)
            bt(i + 1, curr_combo)
            curr_combo.pop()

    ans = []
    bt(0, [])
    return ans


n = 4
k = 2
# Output: [[1, 2], [1, 3], [1, 4], [2, 3], [2, 4], [3, 4]]
# Explanation: There are 4 choose 2 = 6 total combinations.

# n = 3
# k = 3
# Output: [[1,2,3]]
# Explanation: There is only one possible combination since we need to choose all 3 numbers from a set of 3.

# n = 1
# k = 1
# Output: [[1]]
# Explanation: There is 1 choose 1 = 1 total combination.

print(combine_1(n, k))
print(combine_2(n, k))
print(combine_3(n, k))
