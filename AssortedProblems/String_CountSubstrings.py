# Given a string and a substring, return the number of times a substring appears in a string.


def count_substrings(str, substr):
    str_len = len(str)
    substr_len = len(substr)
    num_of_windows = str_len - substr_len + 1
    split_sub = list(sub_string)
    count = 0

    for i in range(num_of_windows):
        sample = [str[ch] for ch in range(i, i + substr_len)]
        if sample == split_sub:
            count += 1

    return count


string = "ABCDCDC"
sub_string = "CDC"
# Output: 2

print(count_substrings(string, sub_string))
