# 0. Find Repeated Character
# Given a string s, return the first character to appear twice.
# It is guaranteed that the input will have a duplicate character.


def repeatedCharacter(s):
    myset = set()
    for i in s:
        if i in myset:
            return i
        myset.add(i)


s = "abcdeda"
# Output: d

print(repeatedCharacter(s))
