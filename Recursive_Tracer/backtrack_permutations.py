# 46. Permutations
# Given an array of distinct integers, return all the possible permutations.
from recursive_tracer import trace_calls, tracer


@trace_calls
def permuts(nums):
    @trace_calls
    def bt(path):
        if len(path) == len(nums):
            ans.append(path[:])
            return

        for i in range(len(nums)):
            if not used[i]:
                used[i] = True
                path.append(nums[i])
                bt(path)
                path.pop()
                used[i] = False

    ans = []
    used = [False] * len(nums)
    bt([])
    return ans


nums = [1, 2, 3]

tracer.reset()
print(permuts(nums))
tracer.generate_svg("backtrack_permutations")
