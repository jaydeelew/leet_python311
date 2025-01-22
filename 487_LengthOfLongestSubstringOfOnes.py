# 487 - Max Consecutive Ones
# You are given a binary substring s (a string containing only "0" and "1").
# An operation involves flipping a "0" into a "1".
# What is the length of the longest substring containing only "1" after performing at most one operation?
# Because the string can only contain "1" and "0", another way to look at this problem is
# "what is the longest substring that contains at most one "0"?".
# This makes it easy for us to solve with a sliding window where our condition is window.count("0") <= 1.
# We can use an integer curr that keeps track of how many "0" we currently have in our window.


def findLength(s):
    # left boudary pointer of window, current qty of zeroes in window, max size of window thus far
    left = curr = ans = 0
    # iterate over s array with right boundary pointer
    for right in range(len(s)):
        # if current postion of right boundary marker points to zero
        if s[right] == "0":
            # increment current qty of zeroes in window
            curr += 1
        # while current qty of zeroes in window is greater than one
        while curr > 1:
            # if left boudary pointer is zero
            if s[left] == "0":
                # decrement current qty of zeroes in window
                curr -= 1
            # move left boundary pointer forward
            left += 1
        # maintain length of largest sub-array (plus one due to being inclusive)
        ans = max(ans, right - left + 1)

    return ans


# s = "10110"
# Output: 4

s = "101101"
# Output: 4

# s = "1101100111"
# Output: 5
# If you perform the operation at index 2, the string becomes 1111100111.

print(findLength(s))
