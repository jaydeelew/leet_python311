# Given a string and a substring, return the number of times a substring appears in a string.


def count_substrings(str, sub):
    count = 0

    for i in range(len(str) - len(sub) + 1):
        if str[i : i + len(sub)] == sub:  # noqa E203
            count += 1

    return count


string = "ABCDCDC"
sub_string = "CDC"
# Output: 2

print(count_substrings(string, sub_string))
