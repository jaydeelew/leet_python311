# 0. Perfect Substring
# A string s comprised of digits from 0 to 9 contains a perfect substring if all the elements
# within a substring occur exactly k times. Calculate the number of perfect substrings in s.
def perfectSubstring(s, k):
    count = 0
    n = len(s)

    for i in range(n):
        freq = [0] * 10  # Since digits are from 0-9
        for j in range(i, n):
            digit = int(s[j])
            freq[digit] += 1

            # If any digit appears more than k times, break early
            if freq[digit] > k:
                break

            # Check if all non-zero counts are exactly k
            if all(f == 0 or f == k for f in freq):
                count += 1

    return count


# Example test case
s = "1102021222"
k = 2
# Output: 6
# Explanation:
# s[0:1] = 11
# s[0:5] = 110202
# s[1:6] = 102021
# s[2:5] = 0202
# s[7:8] = 22
# s[8:9] = 22

print(perfectSubstring(s, k))
