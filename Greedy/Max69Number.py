# 1323. You are given a positive integer num consisting only of digits 6 and 9.
# Return the maximum number you can get by changing at most one digit (6 becomes 9, and 9 becomes 6).


class Solution:
    def maximum69Number(self, num: int) -> int:
        # use list comprehension to convert num to string and iterate over string converting each character to an integer
        int_list = [int(x) for x in str(num)]
        for i in range(len(int_list)):
            if i in range(len(int_list)):
                if int_list[i] == 6:
                    int_list[i] = 9
                    break
        # use list comprehension to iterate over list of integers converting each integer to a string
        str_list = [str(i) for i in int_list]
        # join individual strings in str_list to one string then convert that string to an integer
        return int("".join(str_list))


num = 96699
# Output: 99699

sol = Solution()
print(sol.maximum69Number(num))
