# 0. First Nonadjacent
# Given a string, return the first letter that is nonadjacent with the same letter.


def firstNonAdjacent(s):
    n = len(s)

    if n == 0:
        return None

    # Check the first character if it is not the same as the second one
    if n > 1 and s[0] != s[1]:
        return s[0]
    elif n == 1:
        return s[0]

    # Traverse the string and check adjacent characters
    for i in range(1, n - 1):
        if s[i] != s[i - 1] and s[i] != s[i + 1]:
            return s[i]

    # Check the last character if it is not the same as the second to last one
    if s[-1] != s[-2]:
        return s[-1]

    return None


s = "aabbcdee"

print(firstNonAdjacent(s))
# Output: "c"
