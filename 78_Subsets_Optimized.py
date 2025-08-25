# 78. Subsets - Multiple Efficient Approaches
# Given an integer array nums of unique elements, return all possible subsets (the power set).


def subsets_backtrack_original(nums):
    """Original backtracking approach - O(2^n) time, O(n) space for recursion"""

    def bt(start_index, curr_combo):
        ans.append(curr_combo[:])
        for i in range(start_index, len(nums)):
            curr_combo.append(nums[i])
            bt(i + 1, curr_combo)
            curr_combo.pop()

    ans = []
    bt(0, [])
    return ans


def subsets_iterative_build(nums):
    """Iterative approach - build subsets by adding each element to existing subsets
    O(2^n) time, O(1) extra space (not counting output)"""
    result = [[]]  # Start with empty subset

    for num in nums:
        # For each number, create new subsets by adding it to all existing subsets
        new_subsets = []
        for subset in result:
            new_subsets.append(subset + [num])
        result.extend(new_subsets)

    return result


def subsets_cascading(nums):
    """Cascading approach - most intuitive iterative method
    O(2^n) time, O(1) extra space (not counting output)"""
    subsets = [[]]

    for num in nums:
        # Double the current subsets by adding the new number to each existing subset
        subsets += [curr + [num] for curr in subsets]

    return subsets


def subsets_lexicographic(nums):
    """Lexicographic order generation using binary representation
    O(n * 2^n) time, O(1) extra space"""
    n = len(nums)
    result = []

    for mask in range(2**n):
        subset = []
        for i in range(n):
            if mask & (1 << i):
                subset.append(nums[i])
        result.append(subset)

    return result


def subsets_generator(nums):
    """Generator approach - memory efficient for large datasets
    Yields subsets one at a time instead of storing all in memory"""
    n = len(nums)

    for mask in range(2**n):
        subset = []
        for i in range(n):
            if mask & (1 << i):
                subset.append(nums[i])
        yield subset
