def longest_common_subsequence(s1, s2):
    m, n = len(s1), len(s2)

    # Initialize a 2D array tab where tab[i][j] will hold the length of the longest common subsequence
    # of s1[0:i] and s2[0:j]
    tab = [[0] * (n + 1) for _ in range(m + 1)]

    for i in range(1, m + 1):
        for j in range(1, n + 1):
            # If characters match, extend the length of the common subsequence found so far
            if s1[i - 1] == s2[j - 1]:
                tab[i][j] = tab[i - 1][j - 1] + 1
            else:
                # If no match, take the maximum length by either skipping a character from s1 or s2
                tab[i][j] = max(tab[i - 1][j], tab[i][j - 1])

    # The length of the longest common subsequence is found in tab[m][n]
    return tab[m][n]


s1 = "ABCBDAB"
s2 = "BDCABC"
print(longest_common_subsequence(s1, s2))  # Output: 4
