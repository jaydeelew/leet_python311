# 967. Numbers witht same consecutive differences
# Given two integers n and k, return an array of all the integers of length n where the difference between
# every two consecutive digits is k. You may return the answer in any order.
# Note that the integers should not have leading zeros. Integers as 02 and 043 are not allowed.


class Solution:
    def numsSameConsecDiff(self, n: int, k: int) -> list[int]:
        output = []

        def backtrack(curr_list: list[int]) -> None:
            if len(curr_list) == n:
                # use list comprehension to create list of strings from list of ints
                # since the join function below only works with strings
                s = [str(i) for i in curr_list]
                # use join with empty seperator to combine list of strings into one string
                # then typecast the string to int with int()
                output.append(int("".join(s)))
                return

            # begin by starting nine curr_lists each starting with a number 1 to 9
            for i in range(1, 10):
                if not curr_list:
                    curr_list.append(i)
                    backtrack(curr_list)
                    curr_list.pop()

            # for each curr_list already containing at least one element
            if curr_list:
                # continue building the curr_list by adding elements +k from last element (if within bounds)
                if curr_list[-1] + k < 10:
                    curr_list.append(curr_list[-1] + k)
                    backtrack(curr_list)
                    curr_list.pop()

                # continue building the curr_list by adding elements -k from last element (if within bounds)
                # only run if k > 0 to avoid duplicate entries in the output if k == 0
                if curr_list[-1] - k >= 0 and k > 0:
                    curr_list.append(curr_list[-1] - k)
                    backtrack(curr_list)
                    curr_list.pop()

        backtrack([])
        return output


# n = 3
# k = 7
# Output: [181,292,707,818,929]

# n = 2
# k = 1
# Output: [10,12,21,23,32,34,43,45,54,56,65,67,76,78,87,89,98]

n = 2
k = 0
# Output: [11,22,33,44,55,66,77,88,99]

sol = Solution()
print(sol.numsSameConsecDiff(n, k))
