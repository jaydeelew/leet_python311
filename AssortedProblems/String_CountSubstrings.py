# Given a string and a substring, return the number of times a substring appears in a string.


def kmp_search(main_string, sub_string):
    # Preprocess the pattern (sub_string) to create the lps (longest prefix suffix) array
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

    n = len(main_string)
    m = len(sub_string)
    lps = compute_lps_array(sub_string)
    i = j = 0  # index for main_string and sub_string
    count = 0

    while i < n:
        if sub_string[j] == main_string[i]:
            i += 1
            j += 1

        if j == m:
            count += 1
            j = lps[j - 1]
        elif i < n and sub_string[j] != main_string[i]:
            if j != 0:
                j = lps[j - 1]
            else:
                i += 1

    return count


string = "ABCDCDC"
sub_string = "CDC"
print(kmp_search(string, sub_string))  # Output: 3
