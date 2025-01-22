# 1323. Maximum 69 Number
# You are given a positive integer num consisting only of digits 6 and 9.
# Return the maximum number you can get by changing at most one digit (6 becomes 9, and 9 becomes 6).


def maximum69Number(num: int) -> int:
    str_list = list(str(num))
    for i in range(len(str_list)):
        if str_list[i] == "6":
            str_list[i] = "9"
            break
    return int("".join(str_list))


num = 96699
# Output: 99699

print(maximum69Number(num))
