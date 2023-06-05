# Example 2: You are given a binary substring s (a string containing only "0" and "1").
# An operation involves flipping a "0" into a "1".
# What is the length of the longest substring containing only "1" after performing at most one operation?

# For example, given s = "1101100111", the answer is 5.
# If you perform the operation at index 2, the string becomes 1111100111.

# Because the string can only contain "1" and "0", another way to look at this problem is
# "what is the longest substring that contains at most one "0"?".
# This makes it easy for us to solve with a sliding window where our condition is window.count("0") <= 1.
# We can use an integer curr that keeps track of how many "0" we currently have in our window.


def find_length(s):
    left = curr = ans = 0  # left boudary pointer of window, current qty of zeroes in window, max size of window thus far
    for right in range(len(s)):  # iterate over s array with right boundary pointer
        if s[right] == "0":  # if current postion of right boundary marker points to zero
            curr += 1  # increment current qty of zeroes in window
        while curr > 1:  # while current qty of zeroes in window is greater than one
            if s[left] == "0":  # if left boudary pointer is zero
                curr -= 1  # decrement current qty of zeroes in window
            left += 1  # move left boundary pointer forward
        ans = max(ans, right - left + 1)  # maintain length of largest sub-array (plus one due to being inclusive)

    return ans


s = "1101100111"
print(find_length(s))
