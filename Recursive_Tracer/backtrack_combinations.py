from recursive_tracer import trace_calls, tracer


# Backtracking alone - Naive approach
@trace_calls
def combos_4(n, k):
    @trace_calls
    def bt(start_index):
        if len(curr_build) == k:
            ans.append(curr_build[:])
            return

        for i in range(start_index, n + 1):
            curr_build.append(i)
            bt(i + 1)
            curr_build.pop()

    ans = []
    curr_build = []
    bt(1)
    return ans


n = 4
k = 2
# Output: [[1, 2], [1, 3], [1, 4], [2, 3], [2, 4], [3, 4]]
# Explanation: There are 4 choose 2 = 6 total combinations.

tracer.reset()
print(combos_4(n, k))
tracer.generate_svg("backtrack_combinations")
