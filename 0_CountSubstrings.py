# 0. Count Substrings
# Given a string and a substring, return the number of times a substring appears in a string.


# In the Knuth-Morris-Pratt (KMP) algorithm, lps stands for "longest proper prefix which is also a suffix."
def compute_lps_array(sub_string):
    m = len(sub_string)
    lps = [0] * m
    length = 0
    i = 1

    while i < m:
        if sub_string[i] == sub_string[length]:
            length += 1
            lps[i] = length
            i += 1
        else:
            if length != 0:
                length = lps[length - 1]
            else:
                lps[i] = 0
                i += 1
    return lps


def KMP_search(string, sub_string):
    n = len(string)
    m = len(sub_string)
    lps = compute_lps_array(sub_string)
    i = 0
    j = 0
    count = 0

    while i < n:
        if sub_string[j] == string[i]:
            i += 1
            j += 1

        if j == m:
            count += 1
            j = lps[j - 1]

        elif i < n and sub_string[j] != string[i]:
            if j != 0:
                j = lps[j - 1]
            else:
                i += 1

    return count


string = "ABCDCDC"
sub_string = "CDC"
print(KMP_search(string, sub_string))
